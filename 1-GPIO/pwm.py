import RPi.GPIO as GPIO
import time


GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(28, GPIO.OUT)

GPIO.setup(21, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(27, GPIO.IN)


while True:

    Entrada = GPIO.wait_for_edge(21)

    if Entrada==True:
        GPIO.output(22,True)
        