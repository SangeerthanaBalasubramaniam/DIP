import sys
import cv2
import numpy as np

img = cv2.imread(sys.argv[1])

filter_matrix = np.ones((11,11),np.float32)/(11*11)
dst = cv2.filter2D(img,-1, filter_matrix)

cv2.imwrite("Output.jpg", dst)
cv2.imwrite("Input.jpg", img)
