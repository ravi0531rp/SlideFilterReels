"""
@author : Ravi Prakash
Created on Friday 12 12:54:53 2020
"""

import cv2
import numpy as np 
import datetime
cap = cv2.VideoCapture(0)
ret,init_frame = cap.read()
init_frame = cv2.flip(init_frame,1)

h,w,_ = init_frame.shape
treadLength = 2
start = w

curr = str(datetime.datetime.now()).replace(":","_").replace(".","_").replace(" ","__")

result = cv2.VideoWriter('Slider_' + curr + '.avi' ,  
                         cv2.VideoWriter_fourcc(*'MJPG'), 
                         20, (w,h)) 

prev_frame = init_frame.copy()
while True:
	if start - treadLength <=0:
			break
	ret,frame = cap.read()
	if ret:
		frame = cv2.flip(frame,1)
		frame = cv2.line(frame , (start,0) , (start,h) , (0,255, 0) , 4)
		start = start - treadLength
		init_frame[: , start - treadLength : start , :] = frame[: , start - treadLength : start , :]
		init_frame[: , : start - treadLength , : ] = prev_frame[: , : start - treadLength , :]
		prev_frame = frame.copy()

		temp_init = init_frame.copy()
		temp_init = cv2.line(temp_init , (start,0) , (start,h) , (0,255, 0) , 4)
		
		temp_init = cv2.GaussianBlur(temp_init , (9,9) ,0)
		result.write(temp_init)
		cv2.imshow("frame",temp_init)

		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break 

cap.release()
result.release()
cv2.destroyAllWindows()

cv2.imwrite('Slider_' + curr +'.jpg' , temp_init)
