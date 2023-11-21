a = [2, 3, 4]
b = [2, 5, 6, 10]
c=[]
for i in range(len(a)):
    c.append(a[i]*b[i])
print("La multiplicacié de la llista {} per la llista {} és {}".format(a,b,c))