#records frames using the default camera (argument 0 is passed in VideoCapture)
#can also stream from files
#if 0 doesn't work, try -1
#for using other cameras, use 1, 2, etc.

import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	success, frame = cap.read()
	#success is True if frame is available, else False
	#frame variable captures the frame

	width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
	height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

	cv2.imshow('frame',frame) #show frame

	if cv2.waitKey(1) & 0xFF == ord('q'):
		#if key 'q' is pressed, break
		break

cap.release()
cv2.destroyAllWindows()

print("width = {} and height = {}".format(width, height))
#cap.isOpened() is False if camera index is incorrect, or file-path is wrong