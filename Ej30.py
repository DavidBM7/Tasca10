def mostrar_majors_que(tupla, referencia):
   
    majors_que_referencia = [num for num in tupla if num > referencia]
    print(f'Números majors que {referencia}: {majors_que_referencia}')

def introduir_valors():
   
    valors = []
    while True:
        valor = input("Introdueix un valor enter (o 'q' per sortir): ")
        if valor.lower() == 'q':
            break
        try:
            valors.append(int(valor))
        except ValueError:
            print("Error: Si us plau, introdueix un valor enter.")
    return tuple(valors)

# Programa principal
print("Introdueix els valors de la tupla. Prem 'q' per acabar.")
tupla_valors = introduir_valors()

# Mostrem els majors de 18
mostrar_majors_que(tupla_valors, 18)
