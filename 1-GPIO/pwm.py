import RPi.GPIO as GPIO
import time


GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 1000)
pwm.start(30)


while True:
    pass