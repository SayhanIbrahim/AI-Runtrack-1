# Créer un programme qui lit le contenu du fichier “output.txt” et qui l’affiche dans le terminal
fichier = open('data.txt', 'r')
for line in fichier:
    print(line)
fichier.close()
