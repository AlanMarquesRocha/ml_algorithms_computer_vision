import cv2

cam = cv2.VideoCapture(0)


while(True):
    conectado, img = cam.read()

    cv2.imshow('Face', img)
    cv2.waitKey()

cam.release()
cv2.destroyAllWindows()