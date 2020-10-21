import random
import numpy as np
import matplotlib.pyplot as plt
liste = []
fichier = open('data.txt', 'r')
for line in fichier:
    line = line.lower()
    x = line.split()
    liste.extend(x)
fichier.close()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",  "w",  "x", "y", "z"]

listPremierLetter = []
for mot in liste:
    y = list(mot)
    listPremierLetter.append(y[0])


lenghtOfMots = []
specialCharacters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
for mots in liste:
    for i in mots:
        cnt = 0
        if i in specialCharacters:
            cnt += 1
        x = len(mots) - cnt
        lenghtOfMots.append(x)


matrix = [[0 for x in range(26)] for y in range(26)]

for mot in liste:
    y = len(mot)
    for harf in mot:
        if harf in alphabet:
            x = mot.index(harf)
            i = alphabet.index(harf)
            if x+1 < y:
                letter = mot[x+1]
            else:
                continue
            if letter in alphabet:
                j = alphabet.index(letter)
                matrix[i][j] = matrix[i][j]+1
            else:
                continue


def motgenerateur():
    lst = []
    i = 1
    num = random.choice(lenghtOfMots)
    letter = random.choice(listPremierLetter)
    while i < num:
        lst.append(letter)
        x = alphabet.index(letter)
        lst1 = []
        for index, (value1, value2) in enumerate(zip(matrix[x], alphabet)):
            elmnt1 = value1 * [value2]
            lst1.extend(elmnt1)
        letter = random.choice(lst1)
        i = i+1
    for i in lst:
        print(i, end="")


motgenerateur()
