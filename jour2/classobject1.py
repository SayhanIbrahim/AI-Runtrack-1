class Person:
    def __init__(obj, name, age):
        obj.name = name
        obj.age = age

    def myname(obj):
        print("Hello my name is " + obj.name)

    def myage(obj):
        print("Hello I`m", obj.age, " years old.")


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

p1.myname()
p1.myage()
