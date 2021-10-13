fruit = ('pomme', 'poire', 'ananas', 'banane', 'citron', 'carambole', 'kiwi')

mot = ""
nbLongsMots = 0
for i in range(len(fruit)):
    if len(fruit[i]) >= 7:
        nbLongsMots = nbLongsMots + 1

    mot = fruit[i]
    if mot[0] == 'c':
        print(mot)

print("Il y a " + str(nbLongsMots) + " mot(s) ayant + de 7 lettres")


reponse = ""
for i in range(len(fruit)):
    print(fruit[i])

    reponse = input("Recopie le mot : ")
    
    if reponse.lower() == fruit[i]:
        print("Bravo")
    else:
        print("Ce n'est pas juste, mot juste : " + fruit[i])
