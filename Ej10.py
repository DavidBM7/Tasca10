def mayor(a):
    if a>18:
        print("Es mayor de edad")
    elif a<18:
        print("Es menor de edad")
    else:
        print("Té 18 anys")

#Programari principal
x = int(input("Introdueix la seva edat: "))
mayor(x)
