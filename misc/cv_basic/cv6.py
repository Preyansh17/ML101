import cv2
import numpy as np

img = cv2.imread('messi.jpg')
img = cv2.resize(img, (960, 680))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 0)
imgCanny = cv2.Canny(np.array(img), 150, 200)
imgDilate = cv2.dilate(imgCanny, np.ones((5,5), np.uint8), iterations=3)
cv2.imshow("Gray image", imgGray)
cv2.imshow("Blurred image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dilated image", imgDilate)

cv2.waitKey(0)

