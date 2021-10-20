liste = [1, 2, 3, 4]

def sommeEntiers(liste):
    return sum(liste)

print(sommeEntiers(liste))

def listeDiviseurs(n):
    listeDiviseurs = []
    i = 1

    while i < 30:
        if n % i == 0:
            listeDiviseurs.append(i)
        i = i + 1

    return listeDiviseurs

print(listeDiviseurs(30))

def entierParfait(n):
    listeDiviseursDeN = listeDiviseurs(n)
    somme = 0

    for i in range(len(listeDiviseursDeN)):
        somme = somme + listeDiviseursDeN[i]

    somme = somme - n

    if somme == n:
        return True
    else:
        return False

print(entierParfait(6))
print(entierParfait(16))

def listeEntiersParfaits(b):
    listeEntiersParfaits = []
    i = 0
    
    while i < b:
        if entierParfait(i):
            listeEntiersParfaits.append(i)

    return listeEntiersParfaits

print(listeEntiersParfaits(30))
