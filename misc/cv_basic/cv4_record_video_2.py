#capture video with timer!
import cv2

cap = cv2.VideoCapture(0)

four_cc = cv2.VideoWriter_fourcc(*'I420')
fps = cap.get(cv2.CAP_PROP_FPS)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

out = cv2.VideoWriter('output.avi', four_cc, fps, (int(width),int(height)))
success, frame = cap.read()
time_sec = 5
numFramesRemaining = time_sec*fps - 1

while success and numFramesRemaining > 0:
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	out.write(frame)
	success, frame = cap.read()
	numFramesRemaining -= 1

cap.release()
out.release()
cv2.destroyAllWindows()

#Note: When capturing from multiple cameras at once, use the grab and retrieve methods
#successA = capA.grab()
#successB = capB.grab()
#if successA and successB:
#	frameA = capA.retrieve()
#	frameB = capB.retrieve()
