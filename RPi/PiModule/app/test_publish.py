__author__ = 'suren'
from MsgPublisher import Publisher
from config import Config

pub = Publisher(Config())
pub.publish("Heelo from Rasp publisher 8")
