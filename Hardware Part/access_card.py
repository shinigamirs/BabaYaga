import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


class Read_Access:
    def __init__(self):
        self.reader = SimpleMFRC522()
        self.id = None
        self.text = ""

    def read_access_card(self):
        try:
            self.id, self.text = self.reader.read()


        finally:
            return (self.id)


if __name__ == "__main__":
    read_access = Read_Access()
    id = read_access.read_access_card()
    print("ID:%s" % id)