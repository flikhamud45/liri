def combine_coins(coin, numbers):
    txt = ""
    for x in numbers: txt+= str(coin) + str(x) + ","
    return txt[:-1]

if __name__ == '__main__':
    print(combine_coins('$', range(5)))
