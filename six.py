
import cv2
import sys

path = sys.argv[1]

print ('Path:', path)

#Reads image
img = cv2.imread(path)

if img is None:
    print ("image is not valid")

#saving a copy of the image
cv2.imwrite('copy_of_image.jpg', img)

