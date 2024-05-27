import cv2
import time
import numpy as np

wCam, hCam = 1280, 720
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

while True:
    success, img = cap.read()
    cv2.imshow('img', img)
    cv2.waitKey(1)