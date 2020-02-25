import RPi.GPIO as GPIO
import time

channel=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.OUT)
GPIO.output(channel,GPIO.HIGH)

def scan(self):
    t_end = time.time() + 15
    bar_code = None
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)

    while (t_end > time.time()):

        bar_code = input("Scan the barcode")
        if (bar_code != None):
            break

    print("ISBN:", bar_code)
    time.sleep(1)
    GPIO.output(channel, GPIO.HIGH)

if __name__ == "__main__":
    scan()