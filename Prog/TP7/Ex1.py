def saisieON():
    x = ""

    while not (x == 'oui' or  x == 'non'):
        x = input("Répondez par oui ou par non : ")

    if x == 'oui':
        return 1

    if x == 'non':
        return 0

print(saisieON())
