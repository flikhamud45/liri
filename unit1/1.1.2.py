def edit(s):
    return s+s

def double_letter(my_str):
    return "".join(map(edit, my_str))

if __name__ == '__main__':
    print(double_letter("python"))