import argparse
import sys
import time

import cv2

from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.start()
image = picam2.capture_array()

image = cv2.resize(image, (320, 240))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow('test', image)

