# Créer un programme qui demande a l’utilisateur de renseigner une chaîne de caractères et qui écrit cette chaine de caractere dans un fichier “output.txt”

chaine = input("Entrer vottre nom et prenom: ")
fichier = open('output.txt', 'w')
fichier.write(chaine)
fichier.close()
