from random import randint

def alea(n):
    return randint(1, n)

def aumoins(n):
    pile = 0
    face = 0
    i = 0s

    while not (pile == n and face == n):
        if alea(2) == 1:
            face = face + 1

        elif alea(2) == 2:
            pile = pile + 1

        i = i + 1


aumoins(100)
