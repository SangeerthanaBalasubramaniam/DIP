import sys
import cv2
import numpy
import math

img_path = sys.argv[1]
img_path2 = sys.argv[2]
img = cv2.imread(img_path)
img2 = cv2.imread(img_path2)
h,w,c = img.shape
img2 = cv2.resize(img2, (w,h) )

def weighted(src1, src2, factor):

    image = numpy.zeros(src1.shape,  src1.dtype)

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                image[y,x,c] = int (factor * src1[y,x,c] +  (1.0 - factor) * src2[y,x,c])
                
    return image

factor = 0.5
new_image = weighted(img, img2, factor)

cv2.imwrite("original1.jpg", img)
cv2.imwrite("original2.jpg", img2)
cv2.imwrite("output.jpg", new_image)

