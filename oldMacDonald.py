def hadAFarm():
    return "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n"


def hadAAnimal(animal):
    return "And on that farm he had a " + animal + ", Ee-igh, Ee-igh, Oh!\n"


def hereASound(noise):
    lyrics = ("With a " + noise + ", " + noise + " here and a " + noise + ", " + noise + " there.\n" +
              "Here a " + noise + ", there a " + noise + ", everywhere a " + noise + ", " + noise + ".\n")
    return lyrics


def sing(animal, noise):
    lyrics = hadAFarm() + hadAAnimal(animal) + hereASound(noise) + hadAFarm()
    return lyrics


def main():
    animals = {"pig": "oink",
               "cow": "moo",
               "frog": "croak",
               "dog": "bark",
               "crow": "caw"}

    for i in animals:
        print(sing(i, animals[i]))

main()