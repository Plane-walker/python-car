import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import os

def video_stream():
    camera = PiCamera()
    camera.resolution = (320, 240)
    camera.framerate = 60
    rawCapture = PiRGBArray(camera, size=(320, 240))
    # capture = cv2.VideoCapture(0)
    dir_name, file_name = os.path.split(os.path.abspath(__file__))
    face_xml = cv2.CascadeClassifier(os.path.join(dir_name, "haarcascade_frontalface_alt.xml"))
    # while capture.isOpened():
    #     f, img = capture.read()
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        img = frame.array
        gray = cv2.cvtColor(cv2.resize(img, (160, 120)), cv2.COLOR_BGR2GRAY)
        face = face_xml.detectMultiScale(gray, 1.1, 5)

        for (x,y,w,h) in face:
            cv2.rectangle(img, (x * 2 ,y * 2),(x * 2 + w * 2, y * 2 + h * 2), (255, 0, 0), 2)
        cv2.imshow("viewer", img)
        rawCapture.truncate(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    # capture.release()