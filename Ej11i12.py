def menu_principal():
    print("""
         menu_principal:
            1. Calculadora enteros
            2. Calculadora reales
            3. Canvis de base
            4. salida
    """)
    a = int(input("Elige la opción: "))
    return a
def calculadora_enters():
    op = 1
    while op>0:
        print(""""
            Calculadora de enters
                1. Sumar
                2. Resta
                3. Multiplicación
                4. División
                5. Sortir
              """)
        op = int(input("Elige la opción: "))
        match op:
            case 1: #Sumar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: #Sortir
                print("Adeu, ja tornaras a la calculadora inicial \n\n")
                op=-1
def calculadora_reals():
    print("Calculadora de reals")
    op2 = 1
    while op2>0:
        print(""""
            Calculadora de enters
                1. Sumar
                2. Resta
                3. Multiplicación
                4. División
                5. Sortir
              """)
        op2 = int(input("Elige la opción: "))
        match op2:
            case 1: #Sumar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: #Sortir
                print("Adeu, ja tornaras a la calculadora inicial \n\n")
                op2=-1

#Funcions de canvi de base

#De decimals a altres
def dectobin(numero):
    # Prec: Numero enter
    # Post: Esriu el valor de l'enter en binari
    return bin(numero)

def dectooct(numero):
    # Prec: Numero enter
    # Post: Esriu el valor de l'enter en octal
    return oct(numero)

def dectohex(numero):
    # Prec: Numero enter
    # Post: Esriu el valor de l'enter en hexadecimal
    return hex(numero)

#De binari a altres
def bintodec(numero):
    # Prec: Numero ser cadena de caracters
    # Post: Esriu el valor binari en enter
    a=int(numero,2)
    return a

def bintooct(numero):
    # Prec: Numero ser cadena de caracters
    # Post: Esriu el valor de binari en octal
    a=int(numero,2)
    return oct(numero)

def bintohex(numero):
    # Prec: Numero ser cadena de caracters
    # Post: Esriu el valor de binari en hexadecimal
    a=int(numero,2)
    return hex(numero)
   
#De octal a altres
def octtodec(numero):
    # Prec: Numero ser cadena de caracters
    # Post: Esriu el valor octal en enter
    a=int(numero,8)
    return a

def octtobin(numero):
    # Prec: Numero ser cadena de caracters
    # Post: Esriu el valor de octal en binari
    a=int(numero,8)
    return bin(numero)

def octtohex(numero):
    # Prec: Numero ser cadena de caracters
    # Post: Esriu el valor de octal en hexadecimal
    a=int(numero,8)
    return hex(numero)

#De hexa a altres
def hextodec(numero):
    # Prec: Numero ser cadena de caracters
    # Post: Esriu el valor hex en enter
    a=int(numero,16)
    return a

def hextobin(numero):
    # Prec: Numero ser cadena de caracters
    # Post: Esriu el valor de hex en binari
    a=int(numero,16)
    return bin(numero)

def hextooct(numero):
    # Prec: Numero ser cadena de caracters
    # Post: Esriu el valor de hexa en octal
    a=int(numero,8)
    return hex(numero)

def canvi_base():
    print("Canvi de base")
    op = 1
    while op>0:
        print(""""
            Canvi de base
                1. Donant un binaria ho passem a tota la resta
                2. Donant un octal ho passem a tota la resta
                3. Donant un decimal ho passem a tota la resta
                4. Donant un hexadecimal ho passem a tota la resta
                5. Sortir
              """)
        op = int(input("Elige la opción: "))
        match op:
            case 1: #Binari
                b = int(input("Introdueix un nombre: "))
                o = bintooct(b)
                d = bintodec(b)
                h = bintohex(b)
                print("El numero binari {} es: \n oct -> {} \n dec -> {} \n hex ->".format(b,o,d,h))
            case 2: #Octal
                b = int(input("Introdueix un nombre: "))
                o = octtobin(o)
                d = octtodec(o)
                h = octtohex(o)
                print("El numero octal {} es: \n bin -> {} \n dec -> {} \n hex ->".format(o,b,d,h))
            case 3: #Decimal
                b = int(input("Introdueix un nombre: "))
                o = dectobin(d)
                d = dectooct(d)
                h = dectohex(d)
                print("El numero decimal {} es: \n bin -> {} \n oct -> {} \n hex ->".format(d,b,o,h))
            case 4: #Hexadecimal
                b = int(input("Introdueix un nombre: "))
                o = hextobin(h)
                d = hextooct(h)
                h = hextodec(h)
                print("El numero hexadecimal {} es: \n bin -> {} \n oct -> {} \n dec ->".format(h,b,o,d))
            case 4: #Sortir
                print("Adeu, ja tornaras a la calculadora inicial \n\n")
                op=-1
#Programa principal
a = 1
while a>0:
        a =  menu_principal()
        match a:
            case 1:
                calculadora_enters()
            case 2:
                calculadora_reals()
            case 3:
                canvi_base()
            case 4:
                print("Gràcies, m'en vaig!")
            case other:
                print("Opcion novalida")
#Inicia Calculadora de enteros (si presionas el 1 en el Menú)
