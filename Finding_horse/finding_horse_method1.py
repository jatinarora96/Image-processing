import cv2
import numpy as np
import matplotlib.pyplot as plt


def connected_component_label(path):
    # Getting the input image
    img = cv2.imread(path, 0)
    # Converting those pixels with values 1-127 to 0 and others to 1
    img = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)[1]
    # Applying cv2.connectedComponents()
    num_labels, labels = cv2.connectedComponents(img)

    label_hue = np.uint8(179 * labels / np.max(labels))
    blank_ch = 255 * np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

    # Converting cvt to BGR
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

    # set bg label to black
    labeled_img[label_hue == 0] = 0

    # Showing Original Image
    cv2.imshow('original',cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Showing Image after Component Labeling
    cv2.imshow('horse',cv2.cvtColor(labeled_img, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)

path1 = r'path/to/image'
connected_component_label(path1)