def vocals(x):
    #Si hi ha vocal retorna verdader al cas contrari fals
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
        return True
    else:
        return None
#Llegeix la lletra que introduguis i et dona el resultat
caracter= input("Introdueix una lletra: ")
print(vocals(caracter))
