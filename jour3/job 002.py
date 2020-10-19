# Créer un programme qui parcourt le contenu du fichier “data.txt” et qui compte le nombre de mots(sans caractère spéciaux) qui s’y trouvent
# "Data.txt" dosyasının içeriğine göz atan ve orada bulunan kelime sayısını (özel karakterler olmadan) sayan bir program oluşturun
liste = []
fichier = open('data.txt', 'r')
for line in fichier:
    x = line.split()
    liste.extend(x)

liste2 = []
for mot in liste:
    y = list(mot)
    liste2.extend(y)


print(len(liste))
print(len(liste2))
fichier.close()
