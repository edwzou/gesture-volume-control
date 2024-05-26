import cv2  # used for computer vision tasks
import mediapipe as mp  # pre-trained models for hand gesture recognition, face detection, and more
import time

cap = cv2.VideoCapture(1)  # access webcam here to initialize video capture

mpHands = mp.solutions.hands  # to capture the hand gesture
hands = mpHands.Hands()  # detecting and tracking hand landmarks (fingertips, palm, etc.)
mpDraw = mp.solutions.drawing_utils  # drawing annotations on images

try:
    while True:
        success, img = cap.read()  # captures a frame from webcam
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converts the captured image from BGR color space to RGB color space
        results = hands.process(imgRGB)  # processes the RGB image to detect and track hand landmarks
        # print(results.multi_hand_landmarks)  # print out when hand is detected

        if results.multi_hand_landmarks:  # there exists a hand
            for hand_landmarks in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)  # draw the landmarks and connections

        cv2.imshow('img', img)  # displays the captured frame in a window titled 'img'
        if cv2.waitKey(1) == ord('q'):  # waits for 1 millisecond for a key event, press 'q' to exit
            break

except KeyboardInterrupt:
    print("Interrupted by user")
