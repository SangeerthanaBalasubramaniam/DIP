import sys
import cv2
import numpy
import math

img_path = sys.argv[1] 
img = cv2.imread(img_path) 

resized_img=cv2.resize(img,(180,140), interpolation=cv2.INTER_CUBIC)

cv2.imwrite("bicubic_output.jpg", resized_img)
