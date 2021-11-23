# SlideFilterReels
You see the popular slider filters that they have on Instagram reels or other apps like that, in which the image is getting edited frame by frame with time as per the movement of the line. Well,this is my implementation of the same.

# Dependencies
* Python 3.6
* Opencv 4+
* Numpy 1.19
* playsound 1.2.2

#### <span style="text-decoration:underline">The dependencies are not rigid, but they have been the primary ones for this project. </span>

# Algorithm
* Open the Webcam 
* Read a single frame (init_frame) for 1) reference image 2) getting dimensions of the frames to follow
* flip the image horizontally if your camera gives laterally inverted output
* Set a tread Length , i.e, how many pixels per frame you want your green line to move
* The green vertical line would move from right to Left as they show in the videos
* Initialize the previous frame (prev_frame) to the initial frame we captured. This will keep on getting updated after every loop iteration.
* Create a videoWriter Object to write the video that is created
* Start reading from the camera frame by frame
* But inside the indefinite while loop, write the break condition on top, that is, if the difference between the total width and the distance traversed by the line is <=0.
* Flip the current frame
* replace the ROI of the init_frame with that of our current frame's ROI(the part covered between where our green line is & the right side of the image)
* update the ROI parameter
* replace the rest of init_frame image(Image - ROI) with that of the prev_frame image to maintain fluidity.
* create a duplicate temp variable(temp_init) (from init_frame) for drawing line and showing on screen
* Apply gaussian blur on the modified frames, i.e., temp_init to smoothen the sharp lines created by editing the ROIs.
* Show that frame on screen 
* Save it to disk using the VideoWriter object.
* Save the final modified frame as the resultant image
https://drive.google.com/file/d/17qg_6-i62bjgevTOt_HhTOzeV6MKlSwv/view?usp=sharing
