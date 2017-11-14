#!/usr/bin/python

import os
import datetime
import traceback
import math
import random, string
import base64
import picamera
from time import sleep
from time import gmtime, strftime

def randomword(length):
 return ''.join(random.choice(string.lowercase) for i in range(length))

# Create unique image name
img_name = '/opt/demo/images/pi_image_{0}_{1}.jpg'.format(randomword(3),strftime("%Y%m%d%H%M%S",gmtime()))

# Capture Image from Pi Camera
try:
 camera = picamera.PiCamera()
 camera.annotate_text = " Stored with Apache NiFi "
 camera.capture(img_name, resize=(800,600))

 pass
finally:
 camera.close()
