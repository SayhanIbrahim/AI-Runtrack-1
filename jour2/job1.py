class Personne:
    def __init__(self, nom="SAYHAN", prenom="Ali"):

        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Hello, my name is " + self.nom + " "+self.prenom + ".")


p1 = Personne("Sayhan", "IBRAHIM")
p2 = Personne("Altas", "ISMAIL")
p3 = Personne("Aydin", "ISMAIL")
p4 = Personne("Demir", "HAMDI")
p5 = Personne()
print(p1.nom)
print(p1.prenom)
p1.SePresenter()
p2.SePresenter()
p3.SePresenter()
p4.SePresenter()
p5.SePresenter()

p1.prenom = "Elif"
print(p1.prenom)
p1.SePresenter()
