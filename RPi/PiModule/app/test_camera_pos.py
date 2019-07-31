__author__ = 'suren'
from picamera import PiCamera

try:
    while True:
        cam = PiCamera()
        cam.rotation=180
        cam.start_preview()
except KeyboardInterrupt:
    cam.stop_preview()