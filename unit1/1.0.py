def combine_coins(coin, numbers):
    return "".join([str(coin) + str(x) + "," if x!=4 else str(coin) + str(x) for x in numbers])
if __name__ == '__main__':
    print(combine_coins('$', range(5)))
