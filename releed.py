import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor
import time

# Set up GPIO
relay_pin = 14  # Change this to the GPIO pin connected to your relay
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

def turn_relay_on():
    GPIO.output(relay_pin, GPIO.HIGH)
    print("Relay turned ON")

def turn_relay_off():
    GPIO.output(relay_pin, GPIO.LOW)
    print("Relay turned OFF")

def read_temperature():
    sensor = W1ThermSensor()
    temperature = sensor.get_temperature()
    return temperature

def control_relay():
    while True:
        temperature = read_temperature()
        if temperature >= 20 and temperature <= 25:
            turn_relay_on()
        elif temperature < 20:
            turn_relay_off()
            print("Temperature is below 20 degrees Celsius. Waiting for 2 minutes...")
            time.sleep(120)  # 2 minutes delay
        elif temperature > 25:
            turn_relay_off()
            print("Temperature is above 25 degrees Celsius. Waiting for it to fall within range...")
            while temperature > 25:
                time.sleep(10)  # Check temperature every 10 seconds
                temperature = read_temperature()
            print("Temperature is within range. Turning relay back ON.")
            turn_relay_on()

if __name__ == "__main__":
    try:
        control_relay()
    except KeyboardInterrupt:
        print("\nExiting program")
    finally:
        GPIO.cleanup()
