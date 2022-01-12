import cv2
path1 = r'path/to/image'
img = cv2.imread(path1, 0)
cv2.imshow('original image', img)
rows,cols = img.shape
p = img[90, 290]
r = []
c = []
i = 90
j = 290
#finding the horse by calculating 8 adjacency matrix
for i in range(70,130):
    for j in range(250, 325):
        if (i > 0 and img[i - 1][j] <= 255 and img[i - 1][j] >= 170):
            r.append(i - 1)
            c.append(j)
        if (j > 0 and img[i][j - 1] <= 255 and img[i][j - 1] >= 170):
            r.append(i)
            c.append(j - 1)
        if (i > 0 and j > 0 and img[i - 1][j - 1] <= 255 and img[i - 1][j - 1] >= 170):
            r.append(i - 1)
            c.append(j - 1)
        if (i < rows - 1 and img[i + 1][j] <= 255 and img[i + 1][j] >= 170):
            r.append(i + 1)
            c.append(j)
        if (j < cols - 1 and img[i][j + 1] <= 255 and img[i][j + 1] >= 170):
            r.append(i)
            c.append(j + 1)
        if (i < rows - 1 and j < cols - 1 and img[i + 1][j + 1] <= 255 and img[i + 1][j + 1] >= 170):
            r.append(i + 1)
            c.append(j + 1)
        if (i < rows - 1 and j > 0 and img[i + 1][j - 1] <= 255 and img[i + 1][j - 1] >= 170):
            r.append(i + 1)
            c.append(j - 1)
        if (i > 0 and j < cols - 1 and img[i - 1][j + 1] <= 255 and img[i - 1][j + 1] >= 170):
            r.append(i - 1)
            c.append(j + 1)
for i in range(len(r)):
    p, q = r[i], c[i]
    k = img[p, q]
    img[p, q] = 255
cv2.imshow('Found Horse', img)
cv2.waitKey(0)