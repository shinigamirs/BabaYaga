# import RPi.GPIO as GPIO
# import time
# import sys
#
# channel=21
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(channel,GPIO.OUT)
# GPIO.output(channel,GPIO.HIGH)
#
# def scan(self):
#     t_end = time.time() + 15
#     bar_code = None
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(channel, GPIO.OUT)
#     GPIO.output(channel, GPIO.LOW)
#
#     while (t_end > time.time()):
#         bar_code = input()
#         if (bar_code != None):
#             break
#
#     time.sleep(1)
#     GPIO.output(channel, GPIO.HIGH)
#
#     return bar_code
#
# if __name__ == "__main__":
#     # scan()
#     while(1):
#         command = input()
#         if command != "start":
#             break
#
#         print("status,scanning")
#         sys.stdout.flush() # flushes stdout to be read by parent js process
#
#
#         sys.stdout.flush() # flushes stdout to be read by parent js process