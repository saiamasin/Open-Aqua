import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

def relay_on():
    GPIO.output(13, GPIO.HIGH)

def relay_off():
    GPIO.output(13, GPIO.LOW)

def read_temp_fromfile():
    with open('temperature.txt') as file:
        temperature = float(file.read())
    return temperature

def control_relay():
    while True:
        temperature = read_temp_fromfile()
        if temperature >= 20 and temperature <= 25:
            relay_on()
        elif temperature < 20:
            relay_off()
            # print("Temperature is below 20 degrees Celsius. Waiting for 2 minutes...")
            time.sleep(120)
        elif temperature > 25:
            relay_off()
            # print("Temperature is above 25 degrees Celsius. Waiting for 2 minutes...")
            while temperature > 25:
                time.sleep(10)
                temperature = read_temp_fromfile()
            relay_on()
    
if __name__ == "__main__":
    try:
        control_relay()
    except KeyboardInterrupt:
        print("\nExiting program")
    finally:
        GPIO.cleanup()