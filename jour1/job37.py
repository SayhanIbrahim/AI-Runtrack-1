from itertools import permutations

mot = input("entrer votre mot: ")
length = len(mot)
lst = []
perm = permutations(mot, length)
for i in list(perm):
    lst.append(''.join(i))

lst = sorted(lst)
# print(lst)
indis = lst.index(mot)
print(lst[indis+1])
