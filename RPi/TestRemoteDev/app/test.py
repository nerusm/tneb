__author__ = 'suren'
from picamera import PiCamera
from time import sleep
cam = PiCamera()
cam.rotation=180
cam.start_preview()
sleep(5)
cam.capture('my_image.png')
cam.stop_preview()
print ('Hello')