import RPi.GPIO as GPIO
import time


GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)



while True:
    GPIO.output(12, True)
    time.sleep(0.5)
    GPIO.output(12, False)
    time.sleep(0.5)
