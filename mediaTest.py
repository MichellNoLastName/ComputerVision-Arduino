import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
mp_face = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

with mp_face.FaceMesh(min_detection_confidence = 0.5,min_tracking_confidence = 0.5) as face_mesh:
    while True:
        control,frame = webcam.read()
        if control == False:
            break
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb).multi_face_landmarks
        if result:
            for face_landmarks in result:
                mp_drawing.draw_landmarks(frame,face_landmarks,mp_face.FACEMESH_TESSELATION,landmark_drawing_spec=mp_drawing.DrawingSpec(thickness=1,circle_radius=1,color=(255,0,0)),connection_drawing_spec=mp_drawing.DrawingSpec(thickness=1,color=(0,255,0)))
        cv2.imshow("Test",frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
