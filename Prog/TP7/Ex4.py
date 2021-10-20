from random import randint

def alea(n):
    return randint(1, n)

def aumoins(n):
    pile = 0
    face = 0
    i = 0

    while pile != n and face != n:

        lancer = alea(2)

        if lancer == 1:
            face = face + 1

        elif lancer == 2:
            pile = pile + 1

        i = i + 1

    print("Il aura fallu " + str(i) + " essais pour atteindre " + str(n) + " pile et " + str(n) + " face")

aumoins(100)
