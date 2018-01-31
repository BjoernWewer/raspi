import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
red=11
GPIO.setup(red, GPIO.OUT)
my_pwm=GPIO.PWM(red,100)
my_pwm.start(0)


for q in range(0,6):
	my_pwm.ChangeDutyCycle(2**q)
	time.sleep(0.5)

for q in range(6,0,-1):
	my_pwm.ChangeDutyCycle(2**q)
	time.sleep(0.5)


my_pwm.stop()
GPIO.cleanup()
