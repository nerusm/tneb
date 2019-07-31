__author__ = 'suren'
import RPi.GPIO as G

class GPIO_OP:
    def __init__(self):
        self.green_led = 38
        self.red_led = 37
        print('Init GPIO')
    def __enter__(self):
        G.setmode(G.BOARD)
        G.setup(self.green_led, G.OUT)
        G.setup(self.red_led, G.OUT)
        print('Enter')
        return self
    def __exit__(self, *args):
        # G.cleanup()
        print('Exit')

    def set_led_high(self, led):
        if led == 'GREEN':
            G.output(self.green_led, G.HIGH)
            G.output(self.red_led, G.LOW)
        else:
            G.output(self.green_led, G.LOW)
            G.output(self.red_led, G.HIGH)


