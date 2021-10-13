input1= ""
input2 = ""
input3 = ""

while len(input1) == 0:
    input1 = input("Première note ")

while len(input2) == 0:
    input2 = input("Deuxième note ")

while len(input3) == 0:
    input3 = input("Troisième note ")

moyenne = (float(input1) + float(input2) + float(input3)) / 3

print(moyenne)

somme = float(input1) + float(input2) + float(input3)

if somme >= 40:
    print("Bravo impossible de ne pas valider")

elif somme < 20:
    print("Dommage vous ne pouvez plus valider")

else:
    print("C'est encore possible de valider")



x = 0.0
noteFinale = 0.0

if moyenne < 10:
    while noteFinale < 10:
        noteFinale = (somme + x) / 4
        x = x + 1

print("Pour atteindre les 10 de moyenne, il faudrait une quatrième note de : " + str(x))

mention = input("Quelle mention souhaitez-vous obtenir ? (TB, B, AB, P) ")

TB = 16
B = 14
AB = 12
P = 10

if noteFinale >= 10 and mention == "TB":
    while noteFinale < TB:

