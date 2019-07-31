__author__ = 'suren'
from picamera import PiCamera
from time import sleep
from config import Config
import os
import base64
from MsgPublisher import Publisher
from config import Config

# c = Config()
# print("MQ Server IP: %s" % c.get_env_param('RMQ_SERVER_IP'))
# print("Image save path: %s" % c.get_common_param('IMG_STORE_PATH'))

pub = Publisher(Config())
cam = PiCamera()
cam.rotation=180
cam.start_preview()
sleep(2)
cam.resolution = (800,600)
cam.capture('my_image1.png')
cam.stop_preview()

with open('my_image1.png', 'rb') as image_file:
    str = base64.b64encode(image_file.read())
# print(str)
print('encoded')
if str:
    pub.publish(str)
    fh=open('image_wrtten.png', 'wb')
    fh.write(str.decode('base64'))
    fh.close()
    fh = open('test_str.txt','wb')
    fh.write(str)
    fh.close()
    print('decodeds')

    # fh.flush()
with open("my_image1.png", "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)

# print b
fh = open('test_bytearr.txt','wb')
fh.write(b)
fh.close()
print ('Hello world this is from remote')