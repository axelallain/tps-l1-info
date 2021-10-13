age = input("Quel est votre âge ? ")
sexe = input("Quel est votre sexe ? Répondez par H ou F ")

if sexe == "H" and int(age) >= 20:
    print("Cet habitant est imposable")

elif sexe == "F" and 18 <= int(age) <= 35:
    print("Cet habitant est imposable")

else:
    print("Cet habitant ne paie pas d'impôt")
