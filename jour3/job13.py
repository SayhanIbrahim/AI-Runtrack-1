# Ecrire un programme qui parcours le fichier “data.txt” et qui compte le nombre d’occurence de chaque lettre(Minuscules et Capitales comptent pour la même lettre) en début de mot. A l’aide du module MatPlotLib, générer un histogramme représentant le pourcentage de présence de chaque lettre en début de mot.
# "Data.txt" dosyasını tarayan ve kelimenin başındaki her harfin geçtiği sayıları (Küçük ve Büyük Harfler aynı harf olarak sayılır) sayan bir program yazın. MatPlotLib modülünü kullanarak, bir kelimenin başındaki her harfin var olma yüzdesini temsil eden bir histogram oluşturun.
import matplotlib.pyplot as plt

liste = []
fichier = open('data.txt', 'r')
for line in fichier:
    x = line.split()
    liste.extend(x)

fichier.close()

liste2 = []
for mot in liste:
    y = list(mot)
    liste2.append(y[0])

alphabet = ["Aa", "Bb", "Cc", "Dd", "Ee", "Ff", "Gg", "Hh", "Ii", "Jj", "Kk", "Ll",
            "Mm", "Nn", "Oo", "Pp", "Qq", "Rr", "Ss", "Tt", "Uu", "Vv",  "Ww",  "Xx", "Yy", "Zz"]


liste3 = []
for alfa in alphabet:
    cnt = 0
    for harf in liste2:
        if harf in alfa:
            cnt = cnt + 1
    liste3.append(cnt)

total = sum(liste3)
liste4 = []
for chiffre in liste3:
    cnt = chiffre*100/total
    liste4.append(cnt)


labels = alphabet
sizes = liste4
width = 0.55       # the width of the bars: can also be len(x) sequence
fig, ax = plt.subplots()
ax.bar(labels, sizes, width)
ax.set_ylabel('Percentage')
ax.set_title('Percentage by Letter')
ax.legend()
plt.show()
