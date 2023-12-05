def comprovar_rima(paraula1, paraula2):
    if len(paraula1) < 3 or len(paraula2) < 3:
        return False  # Les paraules han de tenir almenys 3 lletres per a la rima

    if paraula1[-3:] == paraula2[-3:]:
        return "Rimen"
    elif paraula1[-2:] == paraula2[-2:]:
        return "Rimen un poc"
    else:
        return "No rimen"

def main():
    print("Introdueix dues paraules per comprovar si rimen:")
    paraula1 = input("Paraula 1: ").lower()
    paraula2 = input("Paraula 2: ").lower()

    resultat = comprovar_rima(paraula1, paraula2)
    print(resultat)

if __name__ == "__main__":
    main()