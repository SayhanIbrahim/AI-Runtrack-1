# Créer un programme demandant à l’utilisateur de renseigner un nombre entier. Votre programme devra calculer x ^ n, ou n est le nombre fourni par l’utilisateur, sans utiliser de fonction autre que les vôtres. Attention, vous ne devez utiliser ni while, ni for, ni foreach ni … boucle. Seulement de la récursivité.
def factoriyel(base, pover):
    if(pover > 0):
        result = base * factoriyel(base, pover-1)
        print(result)
    else:
        result = 1
    return(result)


base = int(input("Etrer votre numero x pour x^n: "))
pover = int(input(f"Etrer votre numero n pour {base}^n: "))
factoriyel(base, pover)
