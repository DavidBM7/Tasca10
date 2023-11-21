def major(x,y):
    if x>y:
        return x
    else:
        return y
a = int (input("Introdueix el primer nombre: "))
b = int (input("Introdueix el segon nombre: "))
c = major(a,b)
print("El major de {} i {} és {}".format(a,b,a))


#def intercanvi(a,b):
#    return b,a
#x="a"
#y="a"
#print("El valor d'x és {} i el d'y és {}".format(x,y))
#x,y = intercanvi(x,y)
#print("Després de l'intercanvi, el valor d'x és {} i el d'y és {}".format(x,y))