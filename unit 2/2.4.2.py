class BigThing:
    def __init__(self, param):
        self._param = param

    def size(self):
        if isinstance(self._param, int):
            return str(self._param)
        return str(len(self._param))

class BigCat(BigThing):
    def __init__(self, name, weight):
        super().__init__(name)
        self._weight = weight

    def size(self):
        if self._weight <= 15:
            return "OK"
        elif self._weight < 20:
            return "Fat"
        return "Very fat"

cutie = BigCat("mitzy", 22)
print(cutie.size())

my_thing = BigThing(3)
print(my_thing.size())


