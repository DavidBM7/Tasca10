def es_palindrom(paraula):
    paraula = paraula.lower()  # Convertim tots els caràcters a minúscules per considerar majúscules i minúscules equivalents
    return paraula == paraula[::-1]

# Exemples d'ús
print(es_palindrom("radar"))   
print(es_palindrom("air"))     
print(es_palindrom("civic"))  
print(es_palindrom("moix"))  
print(es_palindrom("tapat"))   
print(es_palindrom("casa"))   
print(es_palindrom("refer")) 
