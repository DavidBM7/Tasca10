def canvi(l):
    x=input("Introdueix el valor a inserir al conjunt: ")
    l[x]=int(input("introdueix el nou valor per aquesta clau: "))
#Principal programa
a={"a": 3, "b":5, "c":7, "d":9, "e":10}
print("El valor del conjunt abans de canviar és: {}".format(a))#sin modificar
canvi(a)
print("El valor del conjunt deprés de canviar és: {}".format(a))#modificada

"""
def canvi(l):
    x=input("Introdueix el valor a inserir al conjunt: ")
    l[x]=int(input("introdueix el nou valor per aquesta clau: "))
#Principal programa
a={"a": 3, "b":5, "c":7, "d":9, "e":10}
print("El valor del conjunt abans de canviar és: {}".format(a))#sin modificar
canvi(a)
print("El valor del conjunt deprés de canviar és: {}".format(a))#modificada
"""

"""
#conjunt
def canvi(l):
    x=int(input("Introdueix el valor a inserir al conjunt: "))
    l.add(x)
#Principal programa
a={3, 5, 7, 9, 10}
print("El valor del conjunt abans de canviar és: {}".format(a))#sin modificar
canvi(a)
print("El valor del conjunt deprés de canviar és: {}".format(a))#modificada

"""

"""
#tupla
def canvi(l):
    l = (1, 2, 6, 8)
#Principal programa
a=[3, 5, 7, 9, 10]
print("El valor de la tupla abans de canviar és: {}".format(a))#sin modificar
canvi(a)
print("El valor de la tupla deprés de canviar és: {}".format(a))#modificada
"""

""""
#llista
def canvi(l):
    x = int(input("Introdueix la posicio a modificar: "))#lee la posicion a canviar ( num entero)
    l[x]=input("Introdueix el valor a insertir: ")#el valor que canviara
#Principal programa
a=[3, 4, 5, 6, 7, 8, "a", (1,2), [3,4], 10]
print("El valor de la llista abans de canviar és: {}".format(a))#sin modificar
canvi(a)
print("El valor de la llista deprés de canviar és: {}".format(a))#modificada
"""