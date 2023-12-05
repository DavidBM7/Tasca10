def suma_cuadrados(num):
    if num < 100:
        # Crear una lista de los cuadrados de los números separados por cuatro posiciones
        cuadrados = [(num - i) ** 2 for i in range(0, num, 4)]
        # Calcular la suma de los cuadrados
        suma = sum(cuadrados)
        return suma
    else:
        return None  # Retorna None si el número es mayor o igual a 100

def main():
    # Solicitar al usuario un número
    try:
        numero = int(input("Introduce un número menor de 100: "))
        resultado = suma_cuadrados(numero)

        if resultado is not None:
            print(f"La suma de los cuadrados de los números separados por cuatro posiciones es: {resultado}")
        else:
            print("El número ingresado es mayor o igual a 100.")
    except ValueError:
        print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()