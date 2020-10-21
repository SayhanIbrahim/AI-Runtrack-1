listedata = []
fichier = open('data.txt', 'r')
for line in fichier:
    x = line.split()
    listedata.extend(x)
fichier.close()

listofponctuation = [".", "?", "!", "..."]
listoflenght = dict()
listofsentence = []
for mot in listedata:
    if len(mot) > 0:
        dernierletter = mot[-1]
        if dernierletter in listofponctuation:
            listofsentence.append(mot)
            lenght = len(listofsentence)
            if lenght in listoflenght:
                listoflenght[lenght] += 1
            else:
                listoflenght[lenght] = 1
            listofsentence = []
        else:
            listofsentence.append(mot)
    else:
        continue

print(listoflenght)
