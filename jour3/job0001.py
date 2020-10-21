# Créer un programme qui parcourt le contenu du fichier “domains.xml” et qui compte le nombre d’extension de domain qui s’y trouvent(.com, .net, etc…).
import xml.etree.ElementTree as ET

fichier = ET.parse('domains.xml')
myroot = fichier.getroot()

lst1 = []
for mylist in myroot.iter('column'):
    if len(mylist.text[:]) > 4:
        lst1.append(str(mylist.text[-5:]))

lst2 = []
point = "."
for dmn in lst1:
    x = dmn.split(point)
    lst2.append(x[-1:])

print(lst2)
print(len(lst2))
