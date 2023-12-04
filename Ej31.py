def nums_que_comencen_per(llista_noms, lletra):
    
    noms_comencen_per_lletra = [nom for nom in llista_noms if nom.lower().startswith(lletra.lower())]
    return len(noms_comencen_per_lletra)

# Programa principal
llista_noms = ["Anna", "Albert", "Carlos", "David", "ana", "Alex", "albert"]
lletra_a_comptar = "A"

resultat = nums_que_comencen_per(llista_noms, lletra_a_comptar)
print(f'Hi ha {resultat} noms que comencen per la lletra {lletra_a_comptar}.')