import cv2  # used for computer vision tasks
import mediapipe as mp  # pre-trained models for hand gesture recognition, face detection, and more
import time

cap = cv2.VideoCapture(1)  # access webcam here to initialize video capture

mpHands = mp.solutions.hands  # to capture the hand gesture
hands = mpHands.Hands()  # detecting and tracking hand landmarks (fingertips, palm, etc.)
mpDraw = mp.solutions.drawing_utils  # drawing annotations on images

prevTime = 0
currTime = 0

while True:
    success, img = cap.read()  # captures a frame from webcam
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converts the captured image from BGR color space to RGB color space
    results = hands.process(imgRGB)  # processes the RGB image to detect and track hand landmarks

    if results.multi_hand_landmarks:  # there exists a hand
        for hand_landmarks in results.multi_hand_landmarks:  # a landmark of hand is the pivot point of hand
            for id, landmark in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)  # position of center for each landmark
            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)  # draw the landmarks and connections

    currTime = time.time()  # calculate the frames per second
    fps = 1 / (currTime - prevTime)
    prevTime = currTime

    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 0, 0), 3)  # display fps on screen

    cv2.imshow('img', img)  # displays the captured frame in a window titled 'img'
    if cv2.waitKey(1) == ord('q'):  # waits for 1 millisecond for a key event, press 'q' to exit
        break
