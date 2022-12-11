import functools
def mult_num(id):
    final_lst = []
    for i in range(len(str(id))):
        num = int(str(id)[i])
        result = 0
        if (i+1) % 2 == 0:
            num = num *2
        if num > 9 :
            while num > 0:
                result += num%10
                num = int(num/10)
        else:
            result = num
        final_lst.append(result)
    return final_lst


def check_id_valid(id_number):
    if len(str(id_number)) != 9:
        return False
    return (functools.reduce(lambda x,y : x+y, mult_num(id_number))) % 10 == 0

class IDIterator:
    def __init__(self, id=100000000):
        self._id = id
    def __iter__(self):
        return self
    def __next__(self):
        self._id += 1
        while check_id_valid(self._id) == False and self._id <= 999999999:
            self._id +=1
        if self._id > 999999999:
            raise StopIteration
        cur_id = self._id
        return cur_id

def id_generator(id):
    while True:
        id += 1
        while check_id_valid(id) == False and id <= 999999999:
            id += 1
        yield id


def main():
    id = int(input("Enter id: "))
    gen_iter = input("Generator or Iterator? (gen/it)?: ")
    var = ''
    if gen_iter=="it":
        var = IDIterator(id)
    elif gen_iter=="gen":
        var = id_generator(id)
    try:
        for i in range(10):
            print (next(var))
    except StopIteration:
        print("stop itteration")
    except:
        print("incorrect input")

main()

