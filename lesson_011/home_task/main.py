import AnimalBase
def zoo_announcement(animals):
    for animal in animals:
        print(f"Meet {animal.name}, age {animal.age}. They say:")
        animal.make_sound()
        print()


if __name__ == "__main__":
    lion = AnimalBase.Lion("Simba", 5)
    elephant = AnimalBase.Elephant("Dumbo", 3)
    parrot = AnimalBase.Parrot("Polly", 2)
    eagle = AnimalBase.Eagle("Eddie", 4)

    animals_in_zoo = [lion, elephant, parrot, eagle]
    zoo_announcement(animals_in_zoo)
