def nums_que_comencen_per(llista_noms, lletra):
     #Transforma la llista a minuscula per llegir les paraules que començen per la lletra donada 
    #i imprimeix les que començen per la lletra donada
    noms_comencen_per_lletra = [nom for nom in llista_noms if nom.lower().startswith(lletra.lower())]
    return len(noms_comencen_per_lletra)

# Programa principal
llista_noms = ["Anna", "Albert", "Carlos", "David", "ana", "Alex"]

#introduir la lletra 
lletra_a_comptar = input("Introdueix la lletra per comptar: ")

resultat = nums_que_comencen_per(llista_noms, lletra_a_comptar)
print(f'Hi ha {resultat} noms que comencen per la lletra {lletra_a_comptar}.')

