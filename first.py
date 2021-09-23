import cv2
import sys
path = sys.argv[1]
print ('Path:', path)
#Reads image
img = cv2.imread(path)
if img is None:
 print ("image is not valid")
else:
 print ("image is valid")
img= cv2.resize(img, (100,100))
cv2.imwrite("copy.jpg",img)
