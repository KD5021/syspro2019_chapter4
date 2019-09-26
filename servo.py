import time
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

def setservo(degree):
        set=9.5/180*(90+degree)+2.5
        servo.ChangeDutyCycle(set)
while 1:
	deg=input('please input degree=>')
	if deg>90:
		break
	if deg<-90:
		break
	setservo(deg)
GPIO.cleanup()

