import cv2
import mediapipe as mp
import serial
import math

webcam = cv2.VideoCapture(0) #Open Webcam
mp_face = mp.solutions.face_mesh #mediapipe config
mp_drawing = mp.solutions.drawing_utils
arduino = serial.Serial('COM10',9600) #Serial config

with mp_face.FaceMesh(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as face_mesh:
    while True:
        control, frame = webcam.read()
        if control is False:
            break
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb).multi_face_landmarks
        height,width,channels=frame.shape

        if result:
            for face_landmarks in result:
                point1 = face_landmarks.landmark[306] #Left Lip corner
                x1 = int(point1.x * width)
                y1 = int(point1.y * height)
                cv2.circle(frame,(x1,y1),2,(0,0,255),3)

                point2 = face_landmarks.landmark[61] #Right Lip corner
                x2 = int(point2.x * width)
                y2 = int(point2.y * height)
                cv2.circle(frame,(x2,y2),2,(0,0,255),3)

                distance = math.sqrt(math.pow(y2 - y1,2) + math.pow(x2 - x1,2)) #Distance between lip corners
                print(distance)
                arduino.write(b'A') if distance > 50 else arduino.write(b'B')
        cv2.imshow("Final",frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
