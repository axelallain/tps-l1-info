combien = input("Bonjour, combien de valeurs voulez-vous saisir ? ")

somme = 0
for i in range(int(combien)):
    somme = somme + int(input("Valeur " + str(i+1) + " : "))

moyenne = somme / int(combien)

print(moyenne)
