# Créer un programme qui demande à l’utilisateur de renseigner un nombre entier. Le programme devra alors parcourir le contenu du fichier “data.txt” compter le nombre de mots de la taille renseignée qui s’y trouvent.
import matplotlib.pyplot as plt

liste = []
fichier = open('data.txt', 'r')
for line in fichier:
    x = line.split()
    liste.extend(x)

fichier.close()
liste2 = []
specialCharacters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
for mots in liste:
    for i in mots:
        cnt = 0
        if i in specialCharacters:
            cnt += 1
        x = len(mots) - cnt
        liste2.append(x)

buckle = set(liste2)
liste3 = []
for num in buckle:
    cnt = liste2.count(num)
    liste3.append(cnt)

total = sum(liste3)
liste4 = []
for chiffre in liste3:
    cnt = chiffre*100/total
    liste4.append(cnt)

buckle = list(buckle)
labels = buckle
sizes = liste4
width = 0.40  # the width of the bars: can also be len(x) sequence
fig, ax = plt.subplots()
ax.bar(labels, sizes, width,)
ax.set_ylabel('Percentage')
ax.set_title('Percentage by number of letters')
ax.legend()
plt.show()
