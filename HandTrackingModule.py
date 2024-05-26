import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, hand_landmarks, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNum=0, draw=True):
        landmarkList = []
        if self.results.multi_hand_landmarks:  # there exists a hand
            myHand = self.results.multi_hand_landmarks[handNum]
            for id, landmark in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                landmarkList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
        return landmarkList


def main():
    cap = cv2.VideoCapture(1)  # access webcam here to initialize video capture
    prevTime = 0
    currTime = 0
    detector = handDetector()

    while True:
        success, img = cap.read()  # captures a frame from webcam
        img = detector.findHands(img)
        landmarkList = detector.findPosition(img)
        if len(landmarkList) != 0:
            print(landmarkList[2])

        currTime = time.time()  # calculate the frames per second
        fps = 1 / (currTime - prevTime)
        prevTime = currTime
        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 0, 0), 3)  # display fps on screen

        cv2.imshow('img', img)  # displays the captured frame in a window titled 'img'
        if cv2.waitKey(1) == ord('q'):  # waits for 1 millisecond for a key event, press 'q' to exit
            break

if __name__ == "__main__":
    main()
