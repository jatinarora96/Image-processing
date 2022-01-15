#importing libraries
import cv2
import os
import matplotlib.pyplot as plt 

# Loading the cascade files and also the cascade classifier
def obtaining_cascades():
#     Loading the cascade files
    face_path = os.path.dirname(cv2.data.haarcascades) + '\haarcascade_frontalface_alt2.xml'
    eyes_path = os.path.dirname(cv2.data.haarcascades) + '\haarcascade_eye_tree_eyeglasses.xml'
#     Loading the cascade classifier
    faceCascade = cv2.CascadeClassifier(face_path)
    eyeCascade = cv2.CascadeClassifier(eyes_path)
    return faceCascade, eyeCascade
    
#     Function for reading the image
def reading_image(Name):
    image = cv2.imread('Face.jpg')
    return image

#     Function for displaying the image
def display_image(Image, name, title):
    cv2.imwrite(name, Image)
    plt.figure(figsize=(8, 6), dpi=80)
    plt.imshow(Image)
    plt.title(title)
#     plt.show()
    
    
#     Function for finding the faces    
def find_faces(gray, faceCascade):
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80), flags=cv2.CASCADE_SCALE_IMAGE)
    return faces

#     Function for finding the eyes
def find_eyes(faceROI, eyeCascade):
    eyes = eyeCascade.detectMultiScale(faceROI)
    return eyes


#     Function for crosshair marking the eyecenters and obtaining their centers
def marking(Image_name):
    image = reading_image(Image_name)
    display_image(image, 'Face1.jpg', 'Original Image')
#     converting the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faceCascade, eyeCascade  = obtaining_cascades()
#     Detects faces of different sizes in the input image. The detected faces are returned as a list of rectangles.
    faces = find_faces(gray, faceCascade)
    
    for (x,y,w,h) in faces:
        counter = 0
        cv2.rectangle(image, (x, y), (x + w, y + h),(0,255,0), 2)
        faceROI = image[y:y+h,x:x+w]
#         Detects eyes of different sizes on the faces. The detected eyes are returned as a list of rectangles.
        eyes = find_eyes(faceROI, eyeCascade)
        for (x2, y2, w2, h2) in eyes:
            counter += 1
            if(counter%2 == 0):
                which_eye = 'Right'
            else:
                which_eye = 'Left'
#             Obtaining the center of the eyes.
            eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
#     Radius of the circle that needs to be marked in the center of the eye
            radius = int(round(6*0.25))        
#     Crosshair marking at the center of the eyes
            image = cv2.circle(image, eye_center, radius, (0, 0, 255), 2)
            print('{} eye-centre coordinates: X:{}, Y:{}'.format(which_eye, (x + x2 + w2 // 2),(y + y2 + h2 // 2)))
        name = 'Image_'+str(counter)+'.jpg'
        display_image(image, name, 'Image After Eye-center Detection')


# Calling the Marking function
marking('Result/Face.jpg')