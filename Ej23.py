def crear_punts(llista):
    for num in llista:
        print("." * num)

def dibuixar_imatge(imatge):
    for linia in imatge:
        crear_punts(linia)

# Ejemplo de uso
imatge_a_dibujar = [
    [2, 3, 4, 3, 2],
    [5, 6, 5],
    [2, 2, 2, 2, 2],
    [4, 3, 2, 1, 2, 3, 4]
]

dibuixar_imatge(imatge_a_dibujar)

"""
def crear_punts(llista):
    for num in llista:
        print("." * num)

#Practica principal
crear_punts([2, 3, 4])
"""