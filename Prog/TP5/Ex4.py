from random import randint

def alea(n):
    return randint(1, n)

def calcul(n):
    aleaUn = alea(n)
    aleaDeux = alea(n)

    reponse = int(input("Calculer la somme de " + str(aleaUn) + " et " + str(aleaDeux) + " : "))

    if (aleaUn + aleaDeux) == reponse:
        print("Bravo !")
        return 1
    elif (aleaUn + aleaDeux) != reponse:
        print("La bonne réponse était : " + str((aleaUn+aleaDeux)))
        return 0

calcul(10)


def Serie_calcul(n, nb):
    result = 0

    for i in range(nb):
        result = result + calcul(n)

    print("Score total pour les " + str(nb) + " calculs : " + str(result))

def main():
    n = int(input("Valeur maximale des nombres : "))
    nb = int(input("Nombre de calculs : "))
    Serie_calcul(n, nb)

main()
