# Créer un programme qui modélise un plateau de jeu, carré, de n x n cases. Placez sur ce plateau n dames de manière à ce qu’aucune dame ne puisse se “prendre”, quand cela est possible. La valeur de n est renseignée par l’utilisateur. Quand cela est possible, le programme devra afficher dans le terminal le plateau de jeu avec le caractère ‘O’ pour les cases vides et le caractère ‘X’ pour représenter les dames.
from itertools import permutations, combinations_with_replacement
import numpy as np1


def indexset(num):
    numlist = list(range(num))
    com = combinations_with_replacement(numlist, 2)
    return com


def positionlist(num):
    w, h = num, num
    i = 0
    j = 0
    matrix = [["O" for x in range(w)] for y in range(h)]
    matrix[0][0] = "X"
    if num % 2 == 0:
        for x in range(num-1):
            i = i + 1
            j = j + 2
            if j > (num-1):
                j = j % (num-1)
            matrix[i][j] = "X"
    else:
        for x in range(num-1):
            i = i + 1
            j = j + 2
            if j > (num):
                j = j % (num)
            matrix[i][j] = "X"
    for i in matrix:
        print(i)


num = int(input("Etrer votre numero: "))
positionlist(num)
