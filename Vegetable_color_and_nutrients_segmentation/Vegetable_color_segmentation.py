import cv2
import numpy as np
import matplotlib.pyplot as plt

# Labelling the Vegetables according to the phytonutrients present in them
def label(mask, phytonutrient, value, color):
    ret, residual = cv2.threshold(mask, 0, 255,cv2.THRESH_BINARY)
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(residual, connectivity=8)
    sizes = stats[1:, -1]
    nb_components = nb_components - 1
    min_size = value
    segmented_image = np.zeros((output.shape),dtype = np.uint8)
    for i in range(0, nb_components): #removing small separated areas in the image
        if sizes[i] >= min_size:
            segmented_image[output == i + 1] = 255
#   Getting the contours of the segmented regions
    contours, hierarchy = cv2.findContours(segmented_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    e = 0.01 # Making sure that we don't divide by zero
    for (i,c) in enumerate(contours):
        M= cv2.moments(c)
        cx= int(M['m10']/(M['m00']+e))
        cy= int(M['m01']/(M['m00']+e))
        cv2.putText(img, phytonutrient, org=(cx,cy),
                fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=color,
                thickness=1, lineType=cv2.LINE_AA)

# Detecting the colors of the vegetables
def detect_colors(hsv):
    
#     Detecting Green
    lower_green = np.array([30, 140, 0])
    upper_green = np.array([65, 300, 300])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(img, img, mask = mask_green)
    label(mask_green, "Green(Lutein & Indoles)", 1000, (255, 255, 255))
    
#     Detecting Puple
    lower_purple = np.array([95, -6, 7])
    upper_purple = np.array([176, 220, 219])
    mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)
    res = cv2.bitwise_and(img, img, mask = mask_purple)
    label(mask_purple, "Purple(Anthocyanins & Phenolics)", 1000, (255, 255, 255))
    
#     Detecting Red
    lower_red = np.array([-10, 85, 12])
    upper_red = np.array([7, 265, 300])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(img, img, mask = mask_red)
    label(mask_red, "Red(Lycopene & Anthocyanins)", 1300, (255, 255, 255))
    
#     Detecting Yellow
    lower_yellow = np.array([18, 200, 170])
    upper_yellow = np.array([36, 262, 280])
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(img, img, mask = mask_yellow)
    label(mask_yellow, "Yellow(Carotenoids & Bioflavonoids)", 1000, (0, 0, 0))
    
#     Detecting Orange
    lower_orange = np.array([10, 135, 200])
    upper_orange = np.array([17, 236, 280])
    mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
    res = cv2.bitwise_and(img, img, mask = mask_orange)
    label(mask_orange, "Orange(Beta carotene)", 1100, (0, 0, 0))
    
#     Detecting White
    lower_white = np.array([9, 40, 190])
    upper_white = np.array([30, 110, 293])
    mask_white = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(img, img, mask = mask_white)
    label(mask_white, "White(Allicin)", 1000, (0, 0, 0))

# Reading the image
img = cv2.imread("veg3.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
detect_colors(hsv)
cv2.imshow('Final', img)
cv2.imwrite('Results/veg3.jpg', img)# Saving the image
if cv2.waitKey(0) & 0xFF == ord('q'): 
        cv2.destroyAllWindows()