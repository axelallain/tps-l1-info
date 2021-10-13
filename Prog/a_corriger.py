# definitions de quelques constantes

E = 2.71
isFixed = 1
PI = 3.14159

# petit travail sur une chaine

ch = "python "
ch1 = "est un "
g = ch1[:6]
x = " informatique "
print (ch + g + " langage" + x + "formidable")


#dialogue
n = input("Quel est votre pseudo ?   ")
print ("Bonjour " + n)
a = input(n + ", quelle est votre annee de naissance ?   ")
print("Ah vous avez ", 2021 - int(a), " ans")
print("Au revoir !")
