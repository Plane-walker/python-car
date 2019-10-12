import cv2 as cv

cap = cv.VideoCapture(0)
face_xml = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
while cap.isOpened():
    f, img = cap.read()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face = face_xml.detectMultiScale(gray,1.3,10)

    for (x,y,w,h) in face:
        cv.rectangle(img, (x ,y),(x + w, y + h), (255, 0, 0), 2)
    cv.imshow("1", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()