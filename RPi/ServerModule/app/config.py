import ConfigParser
import os
__author__ = 'suren'

class Config:
    con = ConfigParser.ConfigParser()
    con.read('config.ini')
    env=None
    def __init__(self):
        print("In Config INiti")

        print("Config: %s" % Config.con.get('COMMON', 'IMG_STORE_PATH'))

        try:
            Config.env=os.environ['ENVI']
        except Exception as e:
            print("Exception %s"%e)
            os.environ['ENVI'] = "DEV"
        finally:
            Config.env = os.environ['ENVI']
            print("Co: %s"%Config.env)

    def get_env_param(self,key_name):
        print("In Get Env: %s"%Config.env)
        return str(Config.con.get(Config.env,key_name))
    def get_common_param(self,key_name):
        return str(Config.con.get('COMMON',key_name))