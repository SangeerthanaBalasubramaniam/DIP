import cv2
import numpy as np
import sys

src = cv2.imread(sys.argv[1], 0)
dst = cv2.equalizeHist(src)

cv2.imwrite("Input.jpg", src)
cv2.imwrite("Output.jpg",dst)


