x = input("Entrez une chaîne avec des espaces avant pour que le programme les efface : ")

def deleteEmptySpacesAtTheBeginning(x):
    i = 0
    new = ""

    # On va compter avec i le nombre d'espaces
    # Grâce à ce compteur, on va pouvoir copier la chaine de i jusqu'à la fin de la chaine

    while x[i] == ' ':
        i = i + 1

    new = x[i:]

    return new


print(deleteEmptySpacesAtTheBeginning(x))

