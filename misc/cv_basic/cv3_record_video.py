#to play from a video file instead of capturing live from camera, enter the file name in cv2.VideoCapture() instead of camera index
#eg. cv2.VideoCapture('drop.avi')
#try it!

import cv2

cap = cv2.VideoCapture(0)

four_cc = cv2.VideoWriter_fourcc(*'I420') #FourCC code, cv2.VideoWriter_fourcc('I','4','2','0') is equivalent
fps = cap.get(cv2.CAP_PROP_FPS)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

out = cv2.VideoWriter('output.avi', four_cc, fps, (int(width),int(height)))
#output file name, FourCC code, frames per second and video size

while(cap.isOpened()):
	success, frame = cap.read()

	if(success == True):

		out.write(frame)

		cv2.imshow('frame',frame) #show frame

		if cv2.waitKey(1) & 0xFF == ord('q'):
			#if key 'q' is pressed, break
			break
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()

print("width = {} and height = {}".format(width, height))

#check the documentation for more details!
