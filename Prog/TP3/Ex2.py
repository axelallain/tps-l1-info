chaine = input("Entrez une chaine : ")
caractere1 = input("Entrez le premier caractère : ")
caractere2 = input("Entrez le second caractère : ")

caractere1Counter = 0
caractere2Counter = 0
for i in range(len(chaine)):
    if chaine[i] == caractere1:
        caractere1Counter = caractere1Counter + 1

    elif chaine[i] == caractere2:
        caractere2Counter = caractere2Counter + 1

print("Il y a " + str(caractere1Counter) + " caractère(s) " + caractere1 + " et " + str(caractere2Counter) + " caractère(s) " + caractere2)


for i in range(len(chaine)):
    if chaine[i] == caractere2:
        chaine = chaine[:i] + caractere1 + chaine[i+1:]

    elif chaine[i] == caractere1:
        chaine = chaine[:i] + caractere2 + chaine[i+1:]

print(chaine)
