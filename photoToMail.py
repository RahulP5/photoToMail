from picamera import PiCamera
from time import sleep

import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED_PIN = 13
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(11, GPIO.IN)


def capturePhoto()
	camera = PiCamera()
	camera.start_preview()
	sleep(2)
	camera.capture('/home/pi/Desktop/image.jpg')
	camera.stop_preview()
	camera.close()
	sleep(1)
	sendmail()

def sendmail()
	fromaddr = "example@gmail.com"
	toaddr = "example@gmail.com"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Photo test"
	body = "Photo"
	msg.attach(MIMEText(body, 'plain'))
	filename = "image.jpg"
	attachment = open("/home/pi/Desktop/image.jpg", "rb")

	p = MIMEBase('application', 'octet-stream')
	p.set_payload((attachment).read())
	encoders.encode_base64(p)
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(p)
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(fromaddr, "password")
	text = msg.as_string()
	s.sendmail(fromaddr, toaddr, text)
	s.quit()    
	
while True:
	if GPIO.input(11):
		print("motion detected")
		GPIO.output(LED_PIN, True)
		capturePhoto()
		sleep(1)
	else:
		print("No motion detected")
		GPIO.output(LED_PIN, False)
		
	
