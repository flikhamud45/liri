import functools


def longest_name():
    print(max(open("names.txt", "r").readlines()))


def len_add():
    lst = [len(x) for x in open("names.txt", "r").readlines()]
    print(functools.reduce(lambda x, y: x + y, lst) - len(lst) + 1)


def shortest_name():
    lst = open("names.txt", "r").readlines()
    lst = [sub.replace("\n", "") for sub in lst]
    lst.sort(key= lambda x : len(x))
    print("\n".join([x for x in lst if len(x) == len(lst[0])]))

def create_file():
    f = open("name_length.txt", "w")
    lst = [sub.replace("\n", "") for sub in open("names.txt", "r").readlines()]
    f.write("\n".join([str(len(x)) for x in lst]))

def five():
    lst = [sub.replace("\n", "") for sub in open("names.txt", "r").readlines()]
    num = int(input("put num: "))
    print ("\n".join([x for x in lst if len(x) == num]))


five()
#create_file()
shortest_name()
longest_name()
len_add()
