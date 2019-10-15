import cv2 as cv
import os

def video_stream():
    capture = cv.VideoCapture(0)
    dir_name, file_name = os.path.split(os.path.abspath(__file__))
    face_xml = cv.CascadeClassifier(os.path.join(dir_name, "haarcascade_frontalface_alt.xml"))
    while capture.isOpened():
        f, img = capture.read()
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        face = face_xml.detectMultiScale(gray,1.3,10)

        for (x,y,w,h) in face:
            cv.rectangle(img, (x ,y),(x + w, y + h), (255, 0, 0), 2)
        cv.imshow("1", img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()