def comptar_majuscules(cadena):

    majuscules = sum(1 for lletra in cadena if lletra.isupper())
    return majuscules

# Programa principal
a = "Hola Mon!"
b = "Això és una FRASE amb MAJÚSCULES."
c = "1234 NO TINC MAJÚSCULES."

d = comptar_majuscules(a)
e = comptar_majuscules(b)
f = comptar_majuscules(c)

print(f'Exemple 1: "{a}" Conté {d} lletres majúscules.')
print(f'Exemple 2: "{b}" Conté {e} lletres majúscules.')
print(f'Exemple 3: "{c}" Conté {f} lletres majúscules.')
