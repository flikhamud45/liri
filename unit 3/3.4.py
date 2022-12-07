import string

def check_char_un(username: str):
    flag_ = False
    numflag= False
    letterflag = False
    isok = True
    illegal = []

    for char in username:
        if char == "_":
            flag_ = True
        elif char.isdigit():
            numflag = True
        elif char.isalpha():
            letterflag = True
        else:
            illegal.append(char)

    if not (flag_ and numflag and letterflag) or len(illegal) >0:
        isok = False
    return (illegal, isok)

def check_char_pw(password: str):
    specialflag = False
    lowerflag=False
    numflag= False
    capitalletterflag = False
    isok = True

    for char in password:
        if char.islower():
            lowerflag = True
        elif char.isupper():
            capitalletterflag = True
        elif char.isdigit():
            numflag = True
        elif char in string.punctuation:
            specialflag = True

    if not (specialflag and numflag and lowerflag and capitalletterflag):
        isok = False
    return isok


def check_input(username: str, password):
    x = check_char_un(username)
    y = check_char_pw(password)
    # check username length
    if len(username) < 3:
        raise UsernameTooShort

    elif len(username) > 16:
        raise UsernameTooLong

    # chack username chars

    elif not x[1] :
        raise UsernameContainsIllegalCharacter(x[0])

    # check password chars

    if not y:
        raise PasswordMissingCharacter

    # chech password length

    elif len(password) < 8:
        raise PasswordTooShort

    elif len(password) > 40:
        raise PasswordTooLong

    else :
        print("ok")


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char):
        self._char = char

    def __str__(self):
        return "the username contains illegal chars: " + str(self._char)

class UsernameTooShort(Exception):
    def __str__(self):
        return "username too short."


class UsernameTooLong(Exception):
    def __str__(self):
        return "username too long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "password missing charachter"


class PasswordTooShort(Exception):
    def __str__(self):
        return "password too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "password too long"


#check_input("1", "2")
#check_input("0123456789ABCDEFG", "2")
#check_input("A_a1.", "12345678")
#check_input("A_1", "2")
#check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
#check_input("A_1", "abcdefghijklmnop")
#check_input("A_1", "ABCDEFGHIJLKMNOP")
#check_input("A_1", "ABCDEFGhijklmnop")
#check_input("A_1", "4BCD3F6h1jk1mn0p")
check_input("A_1", "4BCD3F6.1jk1mn0p")
