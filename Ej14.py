def gran_de_tres(num1, num2, num3):
    if num1>num2>num3:
        print(num1)
    elif num2>num1>num3:
        print(num2)
    else:
        print(num3)

#Programari principal
num1= int(input("Introdueix el primer nombre: "))
num2= int(input("Introdueix el segon nombre: "))
num3= int(input("Introdueix el tercer nombre: "))
gran_de_tres(num1, num2, num3)