def send_invitation(name, age):
    if int(age) < 18:
        raise UnderAge(age)
    else:
        print("You should send an invite to " + name)

class UnderAge(Exception):

    def __init__(self, age):
        self._age=age

    def __str__(self):
        return "you are under 18. corrent age:  " + str(self._age)+ " you will bw able to come in: " + str(18-self._age) + " years"

#send_invitation("roni", 17)
send_invitation("yosi", 20)


