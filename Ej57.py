def mostrar(i):
    # Función para mostrar una lista de números en orden descendente
    b = []  # Inicializa una lista vacía para almacenar los números
    for e in range(i, 0, -1):
        b.append(e)  # Agrega cada número al final de la lista
    print(' '.join(map(str, b)))  # Imprime la lista de números como una cadena

# Parte principal del programa
x = int(input("Introdueixi un número petit: "))  # Solicita al usuario un número
for i in range(x, 0, -1):
    mostrar(i)  # Llama a la función mostrar para imprimir listas descendentes

