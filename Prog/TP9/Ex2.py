maliste = [4, 27, -12, -84, 47, 56, 61]

def absolue(maliste):

    for i in range(len(maliste)):
        maliste[i]=(abs(maliste[i]))

    return maliste

print(absolue(maliste))
