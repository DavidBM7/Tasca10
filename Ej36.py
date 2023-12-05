import random

def generar_codi():
    """Genera un codi aleatori de 4 xifres."""
    return [random.randint(0, 9) for _ in range(4)]

def comparar_codis(codi_secret, intent):
    """
    Compara dos codis y retorna el número de números correctes en la posición
    y el número de números correctes però en una posició diferent.

    :param codi_secret: El codi secret a endevinar.
    :param intent: El codi introduït per l'usuari.
    :return: Una tupla amb el número de números correctes y el número de números correctes en una posició diferent.
    """
    correctes_en_posicio = 0
    correctes_no_en_posicio = 0

    for i in range(4):
        if codi_secret[i] == intent[i]:
            correctes_en_posicio += 1
        elif intent[i] in codi_secret:
            correctes_no_en_posicio += 1

    return correctes_en_posicio, correctes_no_en_posicio

def jugar_mastermind():
    """Funció principal per jugar a MasterMind."""
    print("Benvingut a MasterMind!")
    codi_secret = generar_codi()
    intents = 0

    while True:
        intent_usuari = input("Introdueix un codi de 4 xifres (o 'q' per sortir): ")
        
        if intent_usuari.lower() == 'q':
            print(f"El codi secret era {codi_secret}. Fins aviat!")
            break

        try:
            intent_usuari = [int(digit) for digit in intent_usuari]
        except ValueError:
            print("Si us plau, introdueix un codi de 4 xifres o 'q' per sortir.")
            continue

        if len(intent_usuari) != 4 or any(digit < 0 or digit > 9 for digit in intent_usuari):
            print("Si us plau, introdueix un codi de 4 xifres o 'q' per sortir.")
            continue

        intents += 1
        correctes_en_posicio, correctes_no_en_posicio = comparar_codis(codi_secret, intent_usuari)

        print(f"Resultat de l'intent {intents}: {correctes_en_posicio} correctes en posició, {correctes_no_en_posicio} correctes no en posició.")

        if correctes_en_posicio == 4:
            print(f"Enhorabona! Has endevinat el codi en {intents} intents.")
            break

if __name__ == "__main__":
    jugar_mastermind()