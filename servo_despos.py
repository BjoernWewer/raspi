import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
servopin=13
GPIO.setup(servopin, GPIO.OUT)
pwm=GPIO.PWM(servopin,50)
pwm.start(6.5)


for i in range(0,10):
	desiredPosition=input("Which degre you want? (0-180) ")
	DC = 2./45.*(desiredPosition)+2
	pwm.ChangeDutyCycle(DC)

pwm.stop()
GPIO.cleanup()

