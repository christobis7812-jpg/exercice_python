nom = input("Entrez votre Nom et Prénom : ")

age = int(input("Entrez votre âge actuel : "))
travail = int(input("Entrez l'âge que vous aviez lorsque vous avez commencé à travailler : "))

annees_travaillees = age - travail
trimestres_totaux = annees_travaillees * 4
trimestres_manquants = 172 - trimestres_totaux
annees_manquantes = trimestres_manquants // 4

if annees_travaillees >= 43 or age >= 64:
    print(f"Félicitations {nom} ! Vous avez travaillé pendant {annees_travaillees} an(s) "
          f"soit {trimestres_totaux} trimestre(s) au total et vous pouvez partir en retraite.")
else:
    print(f"Courage {nom} ! Vous avez travaillé pendant {annees_travaillees} an(s) "
          f"soit {trimestres_totaux} trimestre(s) au total. "
          f"Vous devez encore travailler {trimestres_manquants} trimestres, soit {annees_manquantes} années avant de partir en retraite.")
