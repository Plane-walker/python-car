import cv2
import os

def video_stream():
    capture = cv2.VideoCapture(0)
    dir_name, file_name = os.path.split(os.path.abspath(__file__))
    face_xml = cv2.CascadeClassifier(os.path.join(dir_name, "haarcascade_frontalface_alt.xml"))
    while capture.isOpened():
        f, img = capture.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = face_xml.detectMultiScale(gray, 1.1, 5)

        for (x,y,w,h) in face:
            cv2.rectangle(img, (x ,y),(x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("viewer", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    capture.release()