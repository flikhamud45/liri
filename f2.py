from file1 import GreetingCard

class BirthdayCard(GreetingCard):
    def __init__(self, senderage = 0 ):
        super().__init__()
        self._sender_age = senderage

    def greeting_msg(self):
        super().greeting_msg()
        print("age: " + str(self._sender_age))