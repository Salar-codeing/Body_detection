import cv2
import mediapipe as mp
import time
from mediapipe.python.solutions import pose

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
pTime = 0

while True:
    success, img = cap.read()
    imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRBG)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    cv2.imshow("Body detection",img)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN,
    3, (255, 0, 0), 3)


    cv2.waitKey(1)