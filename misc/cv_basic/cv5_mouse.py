#using mouse response to stop capturing video

import cv2

clicked = False

def onMouse(event, x, y, flags, param):
	global clicked
	if event == cv2.EVENT_LBUTTONUP:
		#indicates that left mouse button is released
		clicked = True

cap = cv2.VideoCapture(0)
cv2.namedWindow('this window') #create window
cv2.setMouseCallback('this window', onMouse) 

print("Click window or press any key to stop")
success, frame = cap.read()
while success and cv2.waitKey(1) == -1 and not clicked:
	cv2.imshow('this window', frame)
	success, frame = cap.read()

cv2.destroyWindow('this window')
cap.release()

#event - the event that took place, eg. left mouse button pressed
#x, y - coordinates of the event
#flags - relevant flags passed by OpenCV
#params - relevant parameters supplied by OpenCV

#waitKey()  returns the code of the pressed key, or -1 if no key was pressed
#waitKey() only captures input when an OpenCV window has focus
