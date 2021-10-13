from random import randint

def alea(n):
    return randint(1, n)

def lancer(n):
    counter = 0
    for i in range(n):
        flip = randint(1, 2)
        if flip % 2 == 0:
            print("pile")
            counter = counter + 1

    return counter

def main():
    nombreLancers = int(input("Combien de lancers ? "))
    print("Nombre de lancer pile pour ces " + str(nombreLancers) + " lancers : " + str(lancer(nombreLancers)))

main()
