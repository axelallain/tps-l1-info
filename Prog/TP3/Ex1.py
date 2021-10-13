for i in range(10):
        print(str(i+1) + " bonjour\n")

somme = 0
for i in range(100+1):
    somme = somme + i**2
    
print(somme)

result = 1
x = input("Entrez un entier positif : ")
for i in range(1, int(x)+1):
    result = result * i
    
print(result)

entier1 = int(input("Entrez le premier entier : "))
entier2 = int(input("Entrez le second entier : "))

tmp = ""
if entier1 > entier2:
    tmp = entier1
    entier1 = entier2
    entier2 = tmp

sommeCube = 0
for i in range(entier1, entier2+1):
    sommeCube = sommeCube + i**3

print("4 ! = " + str(sommeCube))
