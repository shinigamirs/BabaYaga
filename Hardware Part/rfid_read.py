#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


class Read_Access:
    def __init__(self):
        self.reader = SimpleMFRC522()        
        self.id=None
        self.text=""
    def read_access_card(self):
        try:
            self.id, self.text = self.reader.read()
            
            
        finally:
            GPIO.cleanup()
            return(self.id)

