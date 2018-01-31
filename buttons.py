from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
button1=37
button2=38
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

for q in range(0,5):
	if GPIO.input(button1)==0:
		print("button 1 was pressed")
		sleep(.5)
	if GPIO.input(button2)==0:
		print("button 2 was pressed")
		sleep(.5)

GPIO.cleanup()
