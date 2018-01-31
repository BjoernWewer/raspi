import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
servopin=13
GPIO.setup(servopin, GPIO.OUT)
pwm=GPIO.PWM(servopin,50)
pwm.start(6.5)
r=0


po1=2./45.*(5)+2
po2=2./45.*(180)+2
po3=2./45.*(90)+2

while(r < 3):
	time.sleep(0.5)
	pwm.ChangeDutyCycle(po1)
	time.sleep(0.5)
	pwm.ChangeDutyCycle(po2)
	time.sleep(0.5)
	pwm.ChangeDutyCycle(po3)
	time.sleep(0.5)
	r=r+1

pwm.stop()
GPIO.cleanup()

