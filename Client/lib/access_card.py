# import RPi.GPIO as GPIO
# from mfrc522 import SimpleMFRC522
import time
import sys

# class Read_Access:
#     def __init__(self):
#         self.reader = SimpleMFRC522()
#         self.id = None
#         self.text = ""

#     def read_access_card(self):
#         try:
#             self.id, self.text = self.reader.read()


#         finally:
#             return (self.id)


if __name__ == "__main__":
    # read_access = Read_Access()
    
    while(1):
        command = input()
        if command != "start":
            break

        print("status,scanning")
        sys.stdout.flush() # flushes stdout to be read by parent js process

        time.sleep(1.0)
        # id = read_access.read_access_card()
        
        print("result,123")
        # print("result,ID:%s" % id)

        sys.stdout.flush() # flushes stdout to be read by parent js process