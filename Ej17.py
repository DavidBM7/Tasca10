#Suma de llista 
def sumar_llista(llista):
    suma = 0
    for valor in llista:
        suma += valor
    return suma 
exemple_llista = sumar_llista([1, 2, 3, 4])
print(f"Suma: {exemple_llista}")
#Suma tots el numeros de la llista





# Multiplicació llista
def multiplicar_llista(llista):
    producte = 1
    for valor in llista:
        producte *= valor 
    return producte 
exemple_llista = multiplicar_llista([1, 2, 3, 4])
print(f"Multiplicació: {exemple_llista}")
#Multiplica tots els umeros de la llista