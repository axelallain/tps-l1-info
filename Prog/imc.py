poids = input("Quel est votre poids en kilos ?\n")
taille = input("Quelle est votre taille en mètres ?\n")

imc = float(poids) / (float(taille)**2)
desc = ""

if imc < 16.5:
    desc = "Dénutrition ou famine"

elif 16.5 <= imc <= 18.5:
    desc = "Maigreur"

elif 18.5 <= imc <= 25:
    desc = "Corpulence normale"

elif 25 <= imc <= 30:
    desc = "Surpoids"

elif imc > 30:
    desc = "Obésité"

print("Votre imc est de " + str(imc) + " ce qui vous classe dans : " + desc)

poidsOptimal = taille / x
print("Selon un imc idéal de 23, votre poids optimal serait " + poidsOptimal)
