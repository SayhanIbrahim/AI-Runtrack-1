class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def printlivre(self):
        print(self.titre, "is written by,", self.auteur)


class Personne:
    def __init__(self, nom="NOM", prenom="PRENOM"):

        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Hello, my name is " + self.nom + " " + self.prenom + ".")


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super(Auteur, self).__init__(nom, prenom)
        self.oeuvre = []

    def ecrireUnLivre(self, titre):
        self.oeuvre.append(titre)

    def listerOeuvre(self):
        for i in self.oeuvre:
            print(i)


p1 = Auteur("Demir", "HAMDI")
p1.ecrireUnLivre('fransa')
p1.ecrireUnLivre('turkiye')
p1.ecrireUnLivre('ispanya')
p1.ecrireUnLivre('almanya')
p1.listerOeuvre()
l1 = Livre("Livre 1", "Autheur 1")
l2 = Livre("Livre 2", "Autheur 1")
l3 = Livre("Livre 3", "Autheur 2")
l4 = Livre("Livre 4", "Autheur 2")

l1.printlivre()

print(p1.nom)
print(p1.prenom)
