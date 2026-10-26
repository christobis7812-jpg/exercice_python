s = int(input("Durée en secondes : "))

heures = s // 3600

minutes = (s % 3600) // 60

secondes = s % 60

print(heures, "h", minutes, "min", secondes, "s")