def invertir (cadena):
    #Inverteix la cadena
    return cadena [::-1]
#Programa principal dona la cadena de caracters a invertir
cadena_original = "Soc del Ramis"
cadena_invertida = invertir(cadena_original)
print(cadena_invertida)