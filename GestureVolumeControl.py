import cv2
import time
import numpy as np
import HandTrackingModule as htm
import osascript

wCam, hCam = 640, 480
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.8)

vol = 0
volBar = 400
volPer = 0
volSet = 0
area = 0
colorVol = (0, 0, 0)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    landmarkList, boundingBox = detector.findPosition(img, draw=True)
    if len(landmarkList) != 0:
        area = ((boundingBox[2] - boundingBox[0]) * (boundingBox[3] - boundingBox[1])) // 100
        if 200 < area < 1000:
            length, img, lineInfo = detector.findDistance(4, 8, img)
            vol = np.interp(length, [50, 150], [0, 100])  # map hand range (50 to 200) to volume range (0 to 100)
            volBar = np.interp(length, [50, 150], [400, 150])
            volPer = np.interp(length, [50, 150], [0, 100])
            fingers = detector.fingersUp()
            if not fingers[3]: # detect ring finger because my pinky finger is not that flexible
                volCommand = f"set volume output volume {int(vol)}"   # set volume
                osascript.osascript(volCommand)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                volSet = int(vol)
                colorVol = (0, 255, 0)
            else:
                colorVol = (0, 0, 0)

    cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (128, 128, 128), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (50, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (0, 0, 0), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 40), cv2.FONT_HERSHEY_COMPLEX,
                1, (0, 0, 0), 3)
    cv2.putText(img, f'Vol Set: {int(volSet)}', (420, 40), cv2.FONT_HERSHEY_COMPLEX,
                1, colorVol, 3)

    cv2.imshow('GestureVolumeControl', img)
    if cv2.waitKey(1) == ord('q'):
        break
