
# Aşağıdaki çalışmada kullanıcıdan herhangi bir karakter dizisi girmesini istiyoruz.
# Kodlarımız bize, kullanıcının girdiği karakter dizisi içinde her bir harften kaç tane olduğunu söylüyor:

# replace metodu ile karakter dizisi içindeki boşlukları siliyoruz.
soru = raw_input("Bir karakter dizisi giriniz: ").replace(" ", "")

# Listeleri kullanarak, karakter dizisi içindeki
# çift öğeleri teke indiriyoruz
ortak = list(soru)

# ortak kümesi içindeki öğeleri karakter dizisi içinde kaçar adet geçtiğini buluyoruz.
for i in ortak:
    print "%s harfinden = => %s tane" % (i, soru.count(i))
