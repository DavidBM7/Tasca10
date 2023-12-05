def calcular_capital_final(cantidad_inicial, interes, anos):
    return cantidad_inicial * (1 + interes / 100) ** anos

def main():
    print("Calculadora de Capital Final")
    
    # Solicitar la cantidad inicial
    while True:
        try:
            cantidad_inicial = float(input("Introduce la cantidad inicial (entre 50000€ y 800000€): "))
            if 50000 <= cantidad_inicial <= 800000:
                break
            else:
                print("Por favor, ingresa una cantidad dentro del rango permitido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Solicitar el interés
    while True:
        try:
            interes = float(input("Introduce el interés (entre 0.5% y 13%): "))
            if 0.5 <= interes <= 13:
                break
            else:
                print("Por favor, ingresa un interés dentro del rango permitido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Solicitar el número de años
    while True:
        try:
            anos = int(input("Introduce el número de años (entre 3 y 40): "))
            if 3 <= anos <= 40:
                break
            else:
                print("Por favor, ingresa un número de años dentro del rango permitido.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

    # Calcular y mostrar el capital final
    capital_final = calcular_capital_final(cantidad_inicial, interes, anos)
    print(f"\nEl capital final después de {anos} años será: {capital_final:.2f}€")

if __name__ == "__main__":
    main()
