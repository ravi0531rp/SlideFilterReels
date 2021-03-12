import cv2
import numpy as np 
cap = cv2.VideoCapture(0)
ret,init_frame = cap.read()
init_frame = cv2.flip(init_frame,1)

h,w,_ = init_frame.shape
treadLength = 5
start = w


while True:
	ret,frame = cap.read()
	if ret:
		frame = cv2.flip(frame,1)
		frame = cv2.line(frame , (start,0) , (start,h) , (0,255, 0) , 4)
		start = start - treadLength
		init_frame[: , start - treadLength : start , :] = frame[: , start - treadLength : start , :]
		temp_init = init_frame.copy()
		temp_init = cv2.line(temp_init , (start,0) , (start,h) , (0,255, 0) , 4)
		cv2.imshow("frame",temp_init)

		if start <=0:
			break
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break 

cap.release()
cv2.destroyAllWindows()