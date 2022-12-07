import re


class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        if self._hunger > 0:
            return True
        return False

    def feed(self):
        self._hunger -= 1

    def talk(self):
        pass


class Dog(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")

class Cat(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count = 6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")




class Unicorn(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")

class Dragon(Animal):
    def __init__(self, name, hunger=0, color = "green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")

def main():
    dog1 = Dog("Brownie", 1)
    cat1 = Cat("Zelda", 1)
    skunk1 = Skunk("Stinky")
    unicorn1 = Unicorn("Keith", 1)
    dragon1 = Dragon("Lizzy", 1)

    dog2 = Dog("Doggo", 1)
    cat2 = Cat("Kitty", 1)
    skunk2 = Skunk("Stinky Jr.", 1)
    unicorn2 = Unicorn("Clair", 1)
    dragon2 = Dragon("McFly", 1)

    zoo_lst = []

    zoo_lst.append(dog1)
    zoo_lst.append(cat1)
    zoo_lst.append(skunk1)
    zoo_lst.append(unicorn1)
    zoo_lst.append(dragon1)

    zoo_lst.append(dog2)
    zoo_lst.append(cat2)
    zoo_lst.append(skunk2)
    zoo_lst.append(unicorn2)
    zoo_lst.append(dragon2)

    regex = "<class '__main__.(\w*)'>"

    for animal in zoo_lst:
        animaltype = re.search(regex, str(type(animal))).group(1)
        while animal.is_hungry():
            print(str(animaltype) + " " + animal.get_name())
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal,Skunk):
            animal.stink()
        elif isinstance(animal,Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
        else:
            pass

    print(animal.zoo_name)




main()
