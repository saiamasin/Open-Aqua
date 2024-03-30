import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Read temperature from file  
with open('temperature.txt') as file:
    temperature = float(file.read())
    
# Set temperature range    
max_temp = 25

# Turn relay on if within range
if temperature <= max_temp:
    GPIO.output(18, GPIO.HIGH)
# Turn relay off if outside range  
else:
    GPIO.output(18, GPIO.LOW)
