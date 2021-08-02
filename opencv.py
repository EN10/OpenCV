# import the opencv library
import cv2
# importing os module  
import os
# define a video capture object
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(True):
	# Capture the video frame by frame
	ret, frame = vid.read()
	# Display the resulting frame
	cv2.imshow('frame', frame)

	# Save on pressing space
	if cv2.waitKey(1) & 0xFF == ord(' '): 
		# pwd
		print(os.getcwd()) 
		cv2.imwrite('c1.png',frame)
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
