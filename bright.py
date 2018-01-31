import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
red=11
GPIO.setup(red, GPIO.OUT)
my_pwm=GPIO.PWM(red,100)
my_pwm.start(0)
i = 0

while i < 5:
	bright=input("How bright? (1-6) ")
	my_pwm.ChangeDutyCycle(2**bright)
	i = i + 1
	print(i)

my_pwm.stop()
GPIO.cleanup()
