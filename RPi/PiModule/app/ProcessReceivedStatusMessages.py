__author__ = 'suren'
from app.ReceiveMsg import Consumer
from app.config import Config
import time
import json
from gpio_op import GPIO_OP


class ProcessMessages:
    config = Config()


    def main_method(self):
        with Consumer(self.config, self.config.get_common_param('RMQ_SRV2CLI_QUEUE_NAME'),
                      self.config.get_common_param('RMQ_SRV2PI_ROUTING_KEY')) as con:
            con.consume(self.process_message)
    def process_message(self,body):
        print(body)
        if body:
            status_dict = json.loads(body)

            print(status_dict['Status']) #test sftp
            with GPIO_OP() as gpio_opt:
                if status_dict['Status']:
                    gpio_opt.set_led_high('GREEN')
                else:
                    gpio_opt.set_led_high('RED')
        else:
            print('No Body')


process_messages = ProcessMessages()
process_messages.main_method()