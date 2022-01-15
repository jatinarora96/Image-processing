Implementation Details:
Read the input video.
Get the coordinates of the objects that we need to track.
For every frame of the video,
	o Get the region of interest and convert it to HSV color space.
	o Obtain the mask and the histogram for the region of interest.
	o Define the Termination criteria.
	o Apply the CAMShift function.
	o Get the points of the where the rectangle has to be drawn.
	o Draw the rectangle.
Display the result.