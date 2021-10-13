def retourne(ch):
    new = ""
    for i in range(len(ch)):
        new = new + ch[i-1]
    
    return new

print(retourne("axel"))
