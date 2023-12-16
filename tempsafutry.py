import RPi.GPIO as GPIO
import random

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
sensor_pin = 18

# Simulate getting temperature from sensor
def get_temperature_from_sensor():
    # Simulate sensor reading between 0 and 100
    temperature = random.randint(0, 100)
    return temperature

# Set the temperature range
lower_limit = 20
upper_limit = 30

# Get the current temperature from the sensor
def get_current_temperature():
    GPIO.setup(sensor_pin, GPIO.IN)
    temperature = get_temperature_from_sensor()  # Replace with actual code to read the temperature from the GPIO pin
    GPIO.cleanup(sensor_pin)
    return temperature

current_temperature = get_current_temperature()

# Check if the temperature is within the range
if lower_limit <= current_temperature <= upper_limit:
    switch_status = "on"
else:
    switch_status = "off"

# Print the switch status
print("The switch is", switch_status)