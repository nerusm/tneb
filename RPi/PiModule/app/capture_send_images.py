__author__ = 'suren'
import base64
from MsgPublisher import Publisher
from config import Config
from picamera import PiCamera
from time import sleep
import time
from gpio_op import GPIO_OP

image_list = []

config = Config()


def init_camera():
    cam = PiCamera()
    cam.resolution=( int( config.get_common_param('CAM_RESOLUTION_PIX_X')),int(config.get_common_param('CAM_RESOLUTION_PIX_Y')))
    cam.rotation=int(config.get_common_param('CAM_FRAME_ROTATION'))
    with GPIO_OP() as gpio_opt:
        gpio_opt.set_led_high('RED')
    return cam

def form_filename(img_store_path):
    localtime = time.localtime(time.time())
    timestamp = time.strftime('%d%b%Y%H%M',localtime)
    img_filename = img_store_path+'IMG_'+timestamp
    return img_filename+'.'+config.get_common_param('CAM_STORE_FILEFORMAT')

def capture_image():
    camera.start_preview()
    sleep(int(config.get_common_param('CAM_SLEEP_SECONDS')))
    img_name = form_filename(config.get_common_param('IMG_STORE_PATH'))
    # print(img_name)
    camera.capture(img_name)
    camera.stop_preview()
    image_list.append(img_name)

def convert_image_base64encode(img_filename):
    with open(img_filename,'rb') as image_file:
        b64encoded_string = base64.b64encode(image_file.read())
    return b64encoded_string


camera = init_camera()
capture_image()
publish=Publisher(config, config.get_common_param('RMQ_CLI2SRV_QUEUE_NAME'), config.get_common_param('RMQ_PI2SRV_ROUTING_KEY'))
if image_list:
    print(image_list)
    for image in image_list:
        publish.publish(convert_image_base64encode(image))

print(' [x] Exiting')

