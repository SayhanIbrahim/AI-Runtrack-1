class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myname(self):
        print("Hello my name is " + self.name)

    def myage(self):
        print("Hello I`m", self.age, " years old.")


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

p1.myname()
p1.myage()
