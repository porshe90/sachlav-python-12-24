
class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Some generic animal sound")
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Lion(Mammal):
    def make_sound(self):
        print("Roar!")


class Elephant(Mammal):
    def make_sound(self):
        print("Trumpet!")


class Parrot(Bird):
    def make_sound(self):
        print("Squawk!")


class Eagle(Bird):
    def make_sound(self):
        print("Screech!")
