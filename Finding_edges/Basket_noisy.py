import cv2
import numpy as np
from matplotlib import pyplot as plt


#computing the Mean square error(MSE)
def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2) #formula as given in the book
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def compare_images(imageA, imageB, title):
    # computing the mean squared error(MSE)
    m = mse(imageA, imageB)
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f" %(m))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")
    # show the images
    plt.show()

# Reading images
img0 = cv2.imread('basket_noisy.png',0)
img1 = cv2.imread('gt.png',0)

# remove noise
# convolving with proper kernels
# Gaussian filter
fin1 = cv2.GaussianBlur(img0,(5,5),0)
cv2.imshow("Gaussian",fin1)

# bilateral filter
# fin1 = cv2.bilateralFilter(img0, 5, 75, 75)
# cv2.imshow("bilateral",fin1)

# Operators
# Laplacian operator
fin1 = cv2.Laplacian(fin1,cv2.CV_64F)

# Sobel x operator
# fin2 = cv2.Sobel(img0,cv2.CV_64F,1,0,ksize=5)  # x

# Sobel y filter
# fin3 = cv2.Sobel(img0,cv2.CV_64F, 0,1,ksize=3)  # y

# Canny operator
# fin4 = cv2.Canny(img0,100,200)

# Displaying the results after detcting edges
plt.subplot(1,2,1),plt.imshow(img0,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(fin1,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,2,2),plt.imshow(fin2,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,2,2),plt.imshow(fin3,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,2,2),plt.imshow(fin4,cmap = 'gray')
# plt.title('Canny'), plt.xticks([]), plt.yticks([])

# Generating the Binary Image
ret, bw_img = cv2.threshold(fin1, 12,255,cv2.THRESH_BINARY_INV)

# Comparing the images
compare_images(img1, bw_img, "comparision_with_noise")
plt.show()
# Displaying Binary Image
plt.imshow(bw_img, cmap=plt.cm.gray)
plt.axis("off")
plt.show()