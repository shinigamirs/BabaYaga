import RPi.GPIO as GPIO
import time
from rfid_read import Read_Access   
import signal


    

channel=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.OUT)
GPIO.output(channel,GPIO.HIGH)




read_access=Read_Access()
print("Put your accces card on the reader")
ID=read_access.read_access_card()
print("ID is", ID)
if(ID!=None):
    
    
    
    t_end=time.time()+15
    bar_code=None
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel,GPIO.OUT)
    GPIO.output(channel,GPIO.LOW)
    
    while(t_end>time.time()):
        
        bar_code=input("Scan the barcode")
        if(bar_code!=None):
            break
        
    print("The barcode is ",bar_code)
    time.sleep(1)
    GPIO.output(channel,GPIO.HIGH)
        
