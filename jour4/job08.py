# Créer un programme qui modélise un plateau de jeu, carré, de n x n cases. Placez sur ce plateau n dames de manière à ce qu’aucune dame ne puisse se “prendre”, quand cela est possible. La valeur de n est renseignée par l’utilisateur. Quand cela est possible, le programme devra afficher dans le terminal le plateau de jeu avec le caractère ‘O’ pour les cases vides et le caractère ‘X’ pour représenter les dames.
# N x n kareden oluşan kare bir oyun tahtasını modelleyen bir program oluşturun. Mümkün olduğunda hiçbir dama “yakalanmayacak” şekilde bu tahtaya n tane pul yerleştirin. N'nin değeri kullanıcı tarafından girilir. Mümkün olduğunda, program terminalde oyun tahtasını boş kareler için "O" karakteriyle ve kraliçeleri temsil etmek için "X" karakteriyle göstermelidir.
def dames(num):
    numlst = [0, (num-1)]
    numlst = numlst[:2]+numlst[-2:]
    for i in range(num):
        if i in numlst:
            for j in range(num):
                if j == num-1:
                    if (i+j) % 2 == 0:
                        print("X")
                    else:
                        print("O")
                elif (i+j) % 2 == 0:
                    print("X", end="")
                else:
                    print("O", end="")
        else:
            print(num*"O")


num = int(input("Etrer votre numero: "))
dames(num)
