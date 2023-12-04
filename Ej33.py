def comptar_vocals(paraula):
 
    vocals = "aeiou"
    comptador_vocals = {vocal: paraula.lower().count(vocal) for vocal in vocals}
    return comptador_vocals

# Programa principal
paraula = "Ratapinyada"
resultat = comptar_vocals(paraula)

for vocal, comptador in resultat.items():
    print(f'Hi ha {comptador} "{vocal}" a la paraula "{paraula}".')

