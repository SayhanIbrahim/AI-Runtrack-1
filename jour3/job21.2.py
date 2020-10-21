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

matrixPecentage = [[0.0 for x in range(26)] for y in range(26)]

x = 0
y = 0
for row in matrix:
    y = 0
    cnt = sum(row)
    if cnt != 0:
        for i in row:
            number = matrix[x][y]
            persentage = number*100/cnt
            matrixPecentage[x][y] = round(persentage, 1)
            y = y+1
    x = x+1


harvest = matrixPecentage
fig, ax = plt.subplots()
im = ax.imshow(harvest)

# We want to show all ticks...
ax.set_xticks(np.arange(len(alphabet)))
ax.set_yticks(np.arange(len(alphabet)))
# ... and label them with the respective list entries
ax.set_xticklabels(alphabet)
ax.set_yticklabels(alphabet)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        text = ax.text(j, i, harvest[i][j],
                       ha="center", va="center", color="w")

ax.set_title("Percentage of consecative letters")
fig.tight_layout()
plt.show()
