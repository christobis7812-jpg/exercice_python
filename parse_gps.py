# Étape 1 : Lecture Tolérante & Filtrage des Trames

def lire_et_filtrer_fichier():

    # Déclaration du chemin local du fichier avec la variable "input_file" afin qu'il soit repris dans la suite du code 
    input_file = r"C:\Users\Stagiaire\Downloads\input_log.txt" # Le "r" permet de prendre en compte les slash du chemin local
    lines_filtrees = []

    # Encodage indiqué : latin-1 (pour éviter des erreurs d’encodage du fichier)
    with open(input_file, "r", encoding="latin-1") as fichier:
        for ligne in fichier:
            ligne = ligne.strip()

            # Conserve la ligne qui contient l'une des deux chaînes
            if ("GNSS_ACCESS_LIB" in ligne) or ("Trip Data" in ligne):
                lines_filtrees.append(ligne)

    return lines_filtrees

# si le fichier s'exécute correctement, le programme lit et filtre le fichier, puis affiche combien de lignes ont été conservées.
if __name__ == "__main__":
    lignes = lire_et_filtrer_fichier()
    print(f"[ETAPE 1] Lignes retenues : {len(lignes)}")

# Étape 2 : Parsing Avancé & Gestion des Exceptions

import csv
import re # Importation du module regex pour manipuler du texte à l'aide d'expressions régulières
from pathlib import Path # Importation de la classe Path du module pathlib afin de manipuler les chemins réseaux

# variables donnant le chemin absolu de chaque fichier
input_file = r"C:\Users\Stagiaire\Downloads\input_log.txt"
output_csv = r"C:\Users\Stagiaire\Downloads\output_log.csv"

# Récupération des données brutes dans une liste "records"
def extrairedonneesbrutes(lines):
    records = []
# Création de boucle pour lire chaque ligne : suppression des espaces et indifférence aux lignes vides
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Tentative de parsing CSV des lignes valides et indifférence aux lignes incorrectes.
        try:
            row = next(csv.reader([line], delimiter=",", quotechar='"'))
            if len(row) < 5:
                continue
            
            # Extraction uniquement les champs suivants 
            _index, datestr, heurestr, coordstr, _source = row[:5]

            # Création du timestamp : Date + Heure, avec suppression des microsecondes
            heure_sans_micro = heurestr.split(".", 1)[0].strip()
            timestamp = f"{datestr} {heure_sans_micro}"

            # Extraction des coordonnées : "latitude, longitude " avec les guillemets dans la ligne et altitude = 0 car pas de données présentes dans le fichier
            coordstr = coordstr.strip().strip('"')
            lats_s, lons_s = [x.strip() for x in coordstr.split(",", 1)]

            lat = float(lats_s)
            lon = float(lons_s)
            alt = 0.0

            records.append((timestamp, lat, lon, alt))

        # Si la conversion échoue, cette étape est ignorée.
        except (ValueError, IndexError, StopIteration, csv.Error):
            continue
    # Renvoie la liste de tuples extraits
    return records

# Lecture du fichier originel et application de l'extraction 
with open(input_file, "r", encoding="utf-8", newline="") as f:
    records = extrairedonneesbrutes(f)

# Création du CSV de sortie : output_log.csv, avec un message d'information
out_path = Path(output_csv)

with open(out_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["timestamp", "lat", "lon", "alt"])
    writer.writerows(records)

print("CSV généré :", output_csv, "Nb lignes:", len(records))




