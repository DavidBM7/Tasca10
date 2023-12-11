def esta_ordenada(a):
    b = a.copy()
    a.sort()

    if a == b:
        return "La llista està ordenada de forma no ascendente ni descendente."
    elif a == sorted(b):
        return "La llista està ordenada de forma ascendente."
    elif a == sorted(b, reverse=True):
        return "La llista està ordenada de forma descendente."

def llegir_llista():
    a = []
    c = ""

    while c != ".":
        c = input("Introdueixi un element de la llista i punt (.) per acabar: ")
        if c != ".":
            a.append(int(c))  # Convertir a entero
    return a

# Código principal
a = llegir_llista()
resultat = esta_ordenada(a)
print(resultat)