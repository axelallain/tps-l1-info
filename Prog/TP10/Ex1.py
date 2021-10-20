l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def pairs(l):
    return [x for x in l if x % 2 == 0]

print(pairs(l))

def positions_zero(l):
    return [i for i in range(len(l)) if l[i] == 0]

listeBinaire = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]

print(positions_zero(listeBinaire))

def listeDiviseurs(n):
    return [i for i in range(1,n) if n % i == 0]

print(listeDiviseurs(30))

l1 = [1, 2, 3]
l2 = [4, 5, 6]

def somme(l1, l2):
    return [l1[i] + l2[i] for i in range(len(l1))]

print(somme(l1, l2))

def extrait(c, l):
    return[mot for mot in l if c in mot]

listeMots = ["test", "axel", "avion", "cerise"]

print(extrait("a", listeMots))

l2 = ["a", "b", "c", "d", "e"]

def couple(l1, l2):
    return[l1[i], l2[i] while i < len(l1) or i < len(l2)]

print(couple(l1, l2))
