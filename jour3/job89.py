listedata = []
fichier = open('data.txt', 'r')
for line in fichier:
    line = line.lower()
    x = line.split()
    listedata.extend(x)

fichier.close()

listepokemon = []
fichier = open('listpokemon.txt', 'r')
for line in fichier:
    line = line.lower()
    x = line.split()
    listepokemon.extend(x)

fichier.close()

for mot in listedata:
    if mot in listepokemon:
        print(mot)
        break
    else:
        continue
