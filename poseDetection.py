import cv2
import mediapipe as mp
import serial
import math
import time

webcam = cv2.VideoCapture(0)
webcam.set(3,1280)
webcam.set(4,720)

mp_pose = mp.solutions.pose
arduino = serial.Serial('COM10',9600)
time.sleep(2)

with mp_pose.Pose(static_image_mode=True,min_detection_confidence=0.7,min_tracking_confidence=0.7) as pose:
    while True:
        control, frame = webcam.read()
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        height,width,_ = frame.shape
        result = pose.process(rgb)
        if result.pose_landmarks:
            wrist = result.pose_landmarks.landmark[16]
            x1 = int(wrist.x * width)
            y1 = int(wrist.y * height)
            cv2.circle(frame,(x1,y1),20,(0,0,255),-1)

            elbow = result.pose_landmarks.landmark[14]
            x2 = int(elbow.x * width)
            y2 = int(elbow.y * height)
            cv2.circle(frame,(x2,y2),20,(0,0,255),-1)

            shoulder = result.pose_landmarks.landmark[12]
            x3 = int(shoulder.x * width)
            y3 = int(shoulder.y * height)
            cv2.circle(frame,(x3,y3),20,(0,0,255),-1)

            distance = int(math.sqrt(math.pow(y3 - y1,2) + math.pow(x3 - x1,2))) #Distance between wrist and shoulder
            print(distance)
            if distance > 199 and distance < 500:
                arduino.write(f'{distance}\n'.encode())

        cv2.imshow("Arm Detection",frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
