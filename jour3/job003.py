# Créer un programme qui demande à l’utilisateur de renseigner un nombre entier. Le programme devra alors parcourir le contenu du fichier “data.txt” compter le nombre de mots de la taille renseignée qui s’y trouvent.
liste = []
fichier = open('data.txt', 'r')
for line in fichier:
    x = line.split()
    liste.extend(x)

liste2 = []
specialCharacters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
for mots in liste:
    for i in mots:
        cnt = 0
        if i in specialCharacters:
            cnt += 1
        x = len(mots) - cnt
        liste2.append(x)

num = int(input("Enter votre numero: "))
print(liste2.count(num))
fichier.close()
