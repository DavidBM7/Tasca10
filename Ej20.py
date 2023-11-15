def superposicio(llista1, llista2):
    return bool(set(llista1) & set(llista2))
#Pp
llista_a = [1, 2, 3, 4]
llista_b = [7, 89, 5, 6]

resultado = superposicio(llista_a, llista_b)

print(resultado)
