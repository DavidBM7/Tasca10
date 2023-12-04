def filtrar_paraules(llista_paraules, x):
    paraules_filtrades = [paraula for paraula in llista_paraules if len(paraula) > x]
    return paraules_filtrades

# Programa principal
llista = ["gat", "cotxe", "taula", "ordinador", "sol", "lluna"]
x_minim = 4

resultat = filtrar_paraules(llista, x_minim)
print(resultat)
