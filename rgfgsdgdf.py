a=int(input("Introdueix el primer valor: "))
b=int(input("Introdueix el segon valor: "))
c = a % b
#if c==0:
# print("Es parell")
# else:
# print("Es inparrell")

if a % 2 == 0:
    print("El nombre {} és parell".format(a))
else:
    print("El nombre {} és inparell".format(a))

 
print("L'operació de {} i {} és {}".format(a, b, c))