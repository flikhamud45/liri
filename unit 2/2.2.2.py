class dog:
    count_animals = 0

    def __init__(self, name = "bella"):
        self._name= name
        self._age= 4
        dog.count_animals += 1
    def set_name(self,name):
        self._name = name
    def get_name(self):
        return self._name
    def birthday(self):
        self._age += 1
    def get_age(self):
        return self._age

if __name__ == '__main__':
    dog1 = dog("stacie")
    dog2 = dog()

    print(dog1.get_name() + " " + dog2.get_name())

    dog2.set_name("los")
    print(dog1.get_name() + " " + dog2.get_name())
    print(dog.count_animals)