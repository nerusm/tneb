__author__ = 'suren'
from config import Config
from publish_status import SendStatus

config = Config()
send_status = SendStatus(config=config, status=True, user_name='Suren')
send_status.publish_message()

