def superposicio(llista1, llista2):
    # Convierte las listas en conjuntos para eliminar duplicados y facilitar la operación de intersección
    set_llista1 = set(llista1)
    set_llista2 = set(llista2)

    # Realiza la intersección entre los conjuntos
    interseccio = set_llista1 & set_llista2

    # Convierte el resultado en un valor booleano
    resultat = bool(interseccio)

    # Devuelve True si hay alguna superposición (intersección) y False si no la hay
    return resultat

# Ejemplo de uso con dos listas específicas
llista_a = [1, 2, 3, 4]
llista_b = [7, 89, 5, 6]
resultado = superposicio(llista_a, llista_b)

# Imprime el resultado en la consola
print(resultado)
