Implementation Details:

Read the input video.

Get the coordinates of the objects that we need to track.

For every frame of the video,

	-- Get the region of interest and convert it to HSV color space.
	-- Obtain the mask and the histogram for the region of interest.
	-- Define the Termination criteria.
	-- Apply the CAMShift function.
	-- Draw the rectangle.
    
Display the result.

| Input Object     |  After object detection    |
|------------|-------------|
| ![object](https://user-images.githubusercontent.com/59498809/149622322-9f6fcdc4-59c3-4b60-a070-41007d7beb0f.PNG) | ![4](https://user-images.githubusercontent.com/59498809/149622431-da61de01-aa6c-48b6-8001-84f994164734.PNG)|



