import cv2
import numpy

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	canny = cv2.Canny(frame, 100, 100)
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	sobelX = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
	sobelY = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)

	cv2.imshow('original', frame)
	cv2.imshow('sobelX', sobelX)
	cv2.imshow('sobelY', sobelY)
	cv2.imshow('laplacian', laplacian)
	cv2.imshow('edge', canny)

	if cv2.waitKey(1) & 0xFF == ord('q'):
			#if key 'q' is pressed, break
			break

cv2.destroyAllWindows()
cap.release()

