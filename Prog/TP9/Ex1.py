# La liste contient au moins un 1 et un False
def test1(maliste):
    if 1 in maliste and False in maliste:
        return True
    else:
        return False

maliste = [1, False]

print(test1(maliste))

# La liste contient que des 1 et des False
def test2(maliste):
    if all(p == 1 or p == False for p in maliste):
            return True
    else:
            return False

print(test2(maliste))


listeEntiers = [1, 2, 3, 4, 5, 6, 7, 8]

# Combien d'entiers pairs contient la liste
def combienPairs(maliste):
    nbEntiersPairs = 0

    for i in range(len(maliste)):
        if maliste[i] % 2 == 0:
            nbEntiersPairs = nbEntiersPairs + 1

    return nbEntiersPairs

print("Le nombre d'entiers pairs : " + str(combienPairs(listeEntiers)))

# Retourne une liste des multiples de 3 de la liste donnée
def multiplesTroisDeLaListe(liste_entiers):
    liste_multiples_trois = []

    for i in range(len(liste_entiers)):
        if liste_entiers[i] % 3 == 0:
            liste_multiples_trois.append(liste_entiers[i])

    return liste_multiples_trois

print("Les multiples de 3 : " + str(multiplesTroisDeLaListe(listeEntiers)))

listeAvecDesZeros = [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0]

# Retourne une liste contenant l'indice des zéros de la liste donnée
def positions_zero(listeAvecDesZeros):
    indexDesZeros = []

    for i in range(len(listeAvecDesZeros)):
        if listeAvecDesZeros[i] == 0:
            indexDesZeros.append(i)

    return indexDesZeros

print("Position des zéros : " + str(positions_zero(listeAvecDesZeros)))

listeDoublons = [1, 1, 1, 1]
listeDifferents = [1, 2, 3, 4]

# Retourne True si tous les éléments de la liste sont différents
def listeElementsDifferentsOuNon(liste):
    for i in range(len(liste)):
        if liste[i] in liste[i+1:]:
            return False

    return True

print(listeElementsDifferentsOuNon(listeDoublons)) # Doit retourner False
print(listeElementsDifferentsOuNon(listeDifferents)) # Doit retourner True

def supprime_double(liste):
    listeSansDoublons = []

    for i in range(len(liste)):
        if liste[i] not in listeSansDoublons:
            listeSansDoublons.append(liste[i])

    return listeSansDoublons

print(supprime_double(listeAvecDesZeros))

listeRangee = ["a", "b", "c", "d"]
listeNonRangee = ["b", "a", "d", "c"]

def verifieOrdreAlphabetique(liste):
    for i in range(len(liste)-1):
        # Si dans l'ordre lexicographique, la lettre en cours vient après la suivante
        if liste[i] > liste[i+1]:
            # Alors False, ce n'est pas dans l'ordre alphabétique
            return liste[i]
    # True, cette liste est dans l'ordre alphabétique
    return True

print(verifieOrdreAlphabetique(listeRangee))
print(verifieOrdreAlphabetique(listeNonRangee))
