def masomme(n,p):
    result = 0
    for i in range(n+1):
        result = result + i**p
        
    return result

def main():
    n = int(input("Entrez une limite : "))
    p = int(input("Entrez une puissance : "))

    print(masomme(n,p))

main()
