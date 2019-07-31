__author__ = 'suren'
import RPi.GPIO as g
# for the sleep method
from time import sleep

g_led = 38
r_led = 37
#set numbering mode for the program
g.setmode(g.BOARD)
g.setup(g_led, g.OUT)
g.setup(r_led, g.OUT)
try:
    while True:
      g.output(g_led, g.HIGH)
      g.output(r_led, g.LOW)
      sleep(1)
      g.output(g_led, g.LOW)
      g.output(r_led, g.HIGH)
      sleep(1)

# #setup led(pin 8) as output pin
# GPIO.setup(led, GPIO.OUT, initial=0)
# try:
# #turn on and off the led in intervals of 1 second
#     while (True):
#         #turn on, set as HIGH or 1
#         GPIO.output(led, GPIO.HIGH)
#         print('ON')
#         time.sleep(1)
#         #turn off, set as LOW or 0
#         GPIO.output(led, GPIO.LOW)
#         print('OFF')
#         time.sleep(1)

except KeyboardInterrupt:
    g.cleanup()
    print('Exiting...')
