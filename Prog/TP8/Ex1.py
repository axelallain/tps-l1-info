from random import randint

def saut(n):
    for i in range(n):
        print("\n")

def alea():
    return randint(0, 2)

def affiche(ch):
    new = ""
    for i in range(len(ch)):
        new = new + ch[i] + " "

    return print(new)

affiche("test")

def sansEspaces(ch):
    new = ""
    for i in range(len(ch)):
        if ch[i] != " ":
            new = new + ch[i]

    return new

print(sansEspaces(" b o n j o u r"))


def game():
    lose = False
    chaine = ""
    reponse = ""
    i = 0
    
    while not lose:
        chaine = chaine + str(alea())

        affiche(chaine)

        input("Vous avez mémorisé ? Appuyez sur une touche pour continuer.")

        saut(50)

        reponse = sansEspaces(input("Votre réponse : "))

        i = i + 1

        if reponse == chaine:
            print("Bravo ! On continue.")

        elif reponse != chaine:
            print("Dommage, c'est perdu au bout de " + str(i) + " coups gagnants..\n")
            print("La bonne réponse était : " + chaine)
            lose = True

game()
