import cv2
from picamera2 import Picamera2,Preview
import time


name = 'Caroline' #replace with your name

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QT)
picam2.start()
time.sleep(2)
picam2.capture_file("test.jpg")
