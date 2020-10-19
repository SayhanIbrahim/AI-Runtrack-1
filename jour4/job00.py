# Créer un programme demandant à l’utilisateur de renseigner un nombre entier. Votre programme devra calculer la factorielle de ce nombre, sans utiliser de fonction autre que les vôtres. Attention, vous ne devez utiliser ni while, ni for, ni foreach ni … boucle. Seulement de la récursivité.
def factoriyel(num):
    if(num > 0):
        result = num * factoriyel(num-1)
        print(result)
    else:
        result = 1
    return(result)


num = int(input("Etrer votre numero: "))
factoriyel(num)
