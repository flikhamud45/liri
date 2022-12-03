
def four_dividers(number):
    return list(filter(lambda num: num % 4 == 0, range(1, number)))


print(four_dividers(9))
