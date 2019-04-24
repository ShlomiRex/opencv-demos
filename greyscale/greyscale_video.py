import cv2
import numpy as np
clicked = False
def onMouse(event, x, y, flags, param):
	global clicked
	if event == cv2.cv.CV_EVENT_LBUTTONUP:
		clicked = True

cv2.namedWindow('image capture', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image capture', onMouse)
#initialize the camera object with VideoCapture
camera = cv2.VideoCapture(0)
sucess, frame = camera.read()
cv2.imwrite('snapshot.png', frame)
gray = cv2.imread('snapshot.png', cv2.IMREAD_GRAYSCALE)
while sucess and cv2.waitKey(1) == -1 and not clicked:
	cv2.imwrite('snapshot.png', frame)
	gray = cv2.imread('snapshot.png', cv2.IMREAD_GRAYSCALE)
	cv2.imshow('image capture', gray)
	sucess, frame = camera.read()

cv2.imwrite('snapshot.png', frame)
print('photo taken press any key to exit')
cv2.waitKey()
cv2.destroyAllWindows()