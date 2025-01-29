from animal_base import Lion,Elephant,Parrot,Eagle
def zoo_announcement(animals):
    for animal in animals:
        print(f"Meet {animal.name}, age {animal.age}. They say:")
        animal.make_sound()
        print()


if __name__ == "__main__":
    lion = Lion("Simba", 5)
    elephant = Elephant("Dumbo", 3)
    parrot = Parrot("Polly", 2)
    eagle = Eagle("Eddie", 4)

    animals_in_zoo = [lion, elephant, parrot, eagle]
    zoo_announcement(animals_in_zoo)
