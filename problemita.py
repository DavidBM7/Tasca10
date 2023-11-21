a = []
f = int(input("Introdueix el tamany de la llista: "))
for m in range(f):
    b = input("""
              1. Números
              2. Altres: lletres, llistes, diccionaris, etc.
    """)
    match b:
        case "1":
            a.append(int(input("Introdueix un número: ")))
        case other:
            a.append(input("Introdueix un nou caracter: "))
    a.append(int(input("introdueix un numero:" )))
print(a)