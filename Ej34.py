def es_de_traspas(any):
    """
    Verifica si un any és de traspàs o no.

    :param any: L'any a comprovar.
    :return: True si és de traspàs, False si no ho és.
    """
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        return True
    else:
        return False

# Programa principal
any_a_comprovar = 2032
if es_de_traspas(any_a_comprovar):
    print(f'{any_a_comprovar} és un any de traspàs.')
else:
    print(f'{any_a_comprovar} no és un any de traspàs.')

