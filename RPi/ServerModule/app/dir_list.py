__author__ = 'suren'
import os


for root, dirs, files in os.walk("/home/suren/Projects/TNEB/RPi/ServerModule/known_images/"):
    print(dirs)
    for name in files:
        if name.endswith((".jpeg",".png", ".JPG")):
            print (name)