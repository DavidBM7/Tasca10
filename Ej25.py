def paraula_mes_llarga(llista_paraules):
    if not llista_paraules:
        return None 
    else:
        return max(llista_paraules, key=len)

# Programa principal
llista_paraules = ["Hola", "Ramis", "IES", "Paraula"]

paraula_mes_llarga_resultat = paraula_mes_llarga(llista_paraules)

print(paraula_mes_llarga_resultat)