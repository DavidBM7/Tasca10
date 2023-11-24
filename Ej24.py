def gran_llista(llista):
    if not llista:
        return None  
    else:
        return max(llista)

# Prog princ
llista_nums = [3, 33, 2, 3, 10]

maximo_elemento = gran_llista(llista_nums)

print(maximo_elemento)