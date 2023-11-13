a = 1
while a>0:
    print("""
    Menu:
    1. Mirar si un numero es parell o imparell
    2. Sortir
    """)
    a = int (input("Seleciona una opcio: "))
    match a:
        case 1:
                x = int(input("Introdueix el nombre: "))
                if x % 2==0: 
                        print("El nombre es par")
                else: 
                        print("El nombre es inpar")
        case 2:
                a =0

    