# Nama  : Fadlan Satria Triswanto
# Kelas : D3
# NIM   : 210510001

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Mammal(Animal):

    def __init__(self, name):
        super().__init__(name)

    def give_birth(self):
        pass


class Dog(Mammal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof"


class Cat(Mammal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Meow"


class Poodle(Dog):

    def __init__(self, name, breed, size):
        super().__init__(name, breed)
        self.size = size


my_dog = Poodle("Rocky", "Poodle", "Big")
print(my_dog.name)
print(my_dog.breed)
print(my_dog.size)
print(my_dog.speak())