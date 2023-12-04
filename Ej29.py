def calcular_anys_actual(any_actual, any_naixement):
    
    return any_actual - any_naixement

# Dades
any_actual = 2022
noms = ["Pere", "Maria", "Anna", "Joan"]
anys_naixement = [2000, 1999, 2005, 1990]  # Exemple d'any de naixement

# Capçalera
print("Nom\t\tData naixement\tAnys que farà aquest any")

# Càlcul i impressió de les dades
for nom, any_naixement in zip(noms, anys_naixement):
    anys_fara = calcular_anys_actual(any_actual, any_naixement)
    print(f'{nom}\t\t{any_naixement}\t\t{anys_fara}')
