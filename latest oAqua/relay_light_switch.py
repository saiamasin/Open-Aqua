import datetime
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)

def relay_off():
    print("Relay turned off")
    GPIO.output(22, GPIO.HIGH)

def relay_on():
    print("Relay turned on")
    GPIO.output(22, GPIO.LOW)

def control_relay():
    try:
        with open('form_data.txt') as f:
            lines = f.readlines()
            sisse = lines[0].strip()
            v4lja = lines[1].strip()

        format = "%H:%M"
        V_SISSE = datetime.datetime.strptime(sisse, format)
        V_V4LJA = datetime.datetime.strptime(v4lja, format)

        prg = datetime.datetime.now()
        print(f"Current time: {prg.time()}")
        print(f"On time: {V_SISSE.time()}")
        print(f"Off time: {V_V4LJA.time()}")

        if prg.time() >= V_SISSE.time() and prg.time() <= V_V4LJA.time():
            relay_on()
        else:
            relay_off()

        time.sleep(5)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        while True:
            control_relay()
            print("Sleeping for 1 minute...")
            time.sleep(60)  # Sleep for 1 minute
    except KeyboardInterrupt:
        print("\nExiting program")
    finally:
        GPIO.cleanup()