import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("video3.mp4")
cap.set(3, 1280)
cap.set(4, 720)

mpDraw = mp.solutions.drawing_utils

mpPose = mp.solutions.pose
pose = mpPose.Pose()

pTime = 0
cTime = 0

while True:
    succes, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        landmark_drawing_spec = mpDraw.DrawingSpec(color=(255, 0, 255), thickness=2, circle_radius=2)
        connection_drawing_spec = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2)
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS, landmark_drawing_spec, connection_drawing_spec)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #Muestra los fps
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Body Detector", img)

    cv2.waitKey(1)