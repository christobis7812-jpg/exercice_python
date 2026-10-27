def lire_et_filtrer_fichier():

    # Déclaration du chemin local du fichier avec la variable "input_file" et qu'il soit repris dans la suite du code 
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
