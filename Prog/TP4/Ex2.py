chaine = input("Entrez une chaine : ")

doubles = ""
for i in range(len(chaine)):
    doubles = doubles + chaine[i] + chaine[i]

print(doubles)

i = 0
etoiles = ""
for c in chaine:
    if i % 2 == 0:
        etoiles += c + "*"
    i = i + 1

print(etoiles)

nbEspaces = 0
nbVoyelles = 0
for i in range(len(chaine)):
    if chaine[i] == " ":
        nbEspaces = nbEspaces + 1

    if chaine[i] in ['a', 'e', 'i', 'o', 'u', 'y']:
        nbVoyelles = nbVoyelles + 1

print("Il y a " + str(nbVoyelles) + " voyelles et " + str(nbEspaces) + " espaces")
