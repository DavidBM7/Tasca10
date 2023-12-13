def es_primo(num):
    # Función que verifica si un número es primo
    if num < 2:
        return False  # Los números menores a 2 no son primos
    for i in range(2, num):
        if num % i == 0:
            return False  # Si es divisible por algún número diferente de 1 y sí mismo, no es primo
    return True  # Si no se encontraron divisores, es primo

# Parte principal del programa
nnumersprimers = 0  # Inicializa el contador de números primos
b = []  # Inicializa la lista para almacenar los números primos encontrados

# Itera sobre los números del 1 al 100
for num in range(1, 101):
    if es_primo(num):
        b.append(num)  # Agrega el número primo a la lista
        nnumersprimers += 1  # Incrementa el contador de números primos

# Imprime el resultado
print("Hi ha {} números primers i són {}".format(nnumersprimers, b))

