valeurSuivante = input("Premiere valeur ? ")
somme = 0
i = 0

while valeurSuivante != -1:
    somme = somme + valeurSuivante
    i = i + 1
    valeurSuivante = int(input("Valeur suivante : "))

moyenne = somme / i

print(moyenne) 
