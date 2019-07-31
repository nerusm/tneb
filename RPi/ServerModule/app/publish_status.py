__author__ = 'suren'
from MsgPublisher import Publisher
# from config import Config
import json

class SendStatus:
    def __init__(self, config, status_dict):
        self.config = config
        self.status_dict = status_dict


    def construct_message(self, status_dict):
        msg_literal = "DUM"
        status = status=status_dict['Status']
        user_name=status_dict['Name']
        timestamp = status_dict['Time']
        # print(timestamp)
        # if status:
        #     msg_literal = 'Entry Approved For: %s at %s'% ( user_name, timestamp )
        # else:
        #     msg_literal = 'Entry Denied at %s, try again later'%timestamp
        # print(msg_literal)
        # return msg_literal
        print(json.dumps(status_dict))
        return json.dumps(status_dict)

    def publish_message(self):
        body = self.construct_message(self.status_dict)
        publisher = Publisher(config=self.config,
                              rmq_queue_name=self.config.get_common_param('RMQ_SRV2CLI_QUEUE_NAME'),
                              rmq_routing_key=self.config.get_common_param('RMQ_SRV2PI_ROUTING_KEY'))
        publisher.publish(message=body)

