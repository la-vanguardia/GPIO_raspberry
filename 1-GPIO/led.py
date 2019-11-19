import GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)


while True:
    GPIO.OUT(12, True)
    time.sleep(0.5)
    GPIO.OUT(12, False)
    time.sleep(0.5)
