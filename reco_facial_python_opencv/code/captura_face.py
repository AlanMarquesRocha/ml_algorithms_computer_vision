import cv2

cam = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
    conectado, img = cam.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detected_faces = classifier.detectMultiScale(gray_img,
                                                 scaleFactor = 1.5,
                                                 minSize = (100, 100))

    for (x, y, l, a) in detected_faces:
        cv2.rectangle(img, (x, y), (x + l), (y + a), (0, 0, 2551), 2)

    cv2.imshow('Face', img)
    cv2.waitKey()

cam.release()
cv2.destroyAllWindows()