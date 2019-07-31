__author__ = 'suren'
from app.ReceiveMsg import Consumer
from app.config import Config
import time
from publish_status import SendStatus
from face_rego import Face_Recog

class ProcessMessages:

    config = Config()
    image_list = []
    def main_method(self):
        with Consumer(self.config, self.config.get_common_param('RMQ_CLI2SRV_QUEUE_NAME'), self.config.get_common_param('RMQ_PI2SRV_ROUTING_KEY')) as con:
            con.consume(self.process_message)

    def form_filename(self,img_store_path):
        localtime = time.localtime(time.time())
        timestamp = time.strftime('%d%b%Y%H%M%S',localtime)
        img_filename = img_store_path+'IMG_'+timestamp
        return img_filename+'.'+self.config.get_common_param('CAM_STORE_FILEFORMAT')

    def process_message(self,body):
        image_filename = self.form_filename(self.config.get_common_param('IMG_STORE_PATH'))
        self.save_b64_image(image_filename,body)


    def save_b64_image(self, image_filename, body):
        print(body)
        if body:
            fh=open(image_filename, 'wb')
            fh.write(body.decode('base64'))
            fh.close()
        print(" [x] Image Saved: %s"%image_filename)
        self.image_list.append(image_filename)
        status_dict = self.do_security_check(image_file_name=image_filename)
        self.send_status_2pi(status_dict)

    def send_status_2pi(self, status_dict):
        send_status = SendStatus(config=self.config, status_dict=status_dict)
        send_status.publish_message()

    def do_security_check(self, image_file_name):
        self.fr = Face_Recog(image_name=image_file_name)
        localtime = time.localtime(time.time())
        timestamp = time.strftime('%d-%b-%Y %H:%M:%S',localtime)
        # dict = {'Name': 'Suren', 'Status': True, 'Time' : timestamp}
        dict = self.fr.main_method()

        return dict


process_messages = ProcessMessages()
process_messages.main_method()