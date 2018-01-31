import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

red=11
GPIO.setup(red,GPIO.OUT)

i = input("how often? ")
b = input("how fast? ")
c = 0

for q in range(0,i):
    GPIO.output(red, 1)
    time.sleep(b)
    GPIO.output(red, 0)
    time.sleep(b)
    c = c + 1
    print(c)

GPIO.cleanup()

