import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
servopin=13
GPIO.setup(servopin, GPIO.OUT)
pwm=GPIO.PWM(servopin,50)
pwm.start(6.5)
r=0
time.sleep(0.5)

while(r<3):
	r=r+1
	for i in range(0,180):
		DC = 2./45.*(i)+2
		pwm.ChangeDutyCycle(DC)
		time.sleep(0.01)

	for i in range(180,0,-1):
		DC = 2./45.*(i)+2
		pwm.ChangeDutyCycle(DC)
		time.sleep(0.01)
pwm.stop()
GPIO.cleanup()

