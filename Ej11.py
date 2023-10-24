def menu_principal():
    print("""
        Menu principal:
            1. Calculadora enters
            2. Calculadora reals
            3. Surtir
          """)
    x = int(input("Elegir una opcio: "))
    if x>0 and x<4:
        return x
    else:
        return 0


#Programa
x = menu_principal()