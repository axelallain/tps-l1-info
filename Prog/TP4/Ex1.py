n = 2
somme = 0
for x in range(63+1):
    somme = somme + n**x

print("Cela fait " + str(somme) + " graines")

entiers = tuple(input("Entrez les entiers sans espace : "))
print(entiers)

sommeTuple = 0
for i in range(len(entiers)):
    sommeTuple = sommeTuple + int(entiers[i])

print("La somme des entiers du tuple est : " + str(sommeTuple))
