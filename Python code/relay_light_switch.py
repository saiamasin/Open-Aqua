import datetime
import requests
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

def relay_on():
    GPIO.output(22, GPIO.HIGH)

def relay_off():
    GPIO.output(22, GPIO.LOW)

while True:
  on_time = requests.get('http://localhost:8080/getTime').text

  # convert and check time
  now = datetime.datetime.now()

  if now > on_time:
    relay_on()  
  else:
    relay_off()

  time.sleep(5) 
