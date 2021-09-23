import cv2
import sys

path = sys.argv[1]

print ('Path:', path)

#Reads image
img = cv2.imread(path)

if img is None:
    print ("image is not valid")

h, w, c = img.shape

print (f'     width:  {w}')
print (f'    height:  {h}')
print (f'  channels:  {c}')

img_blur = cv2.blur(img, (25,25))
cv2.imwrite("blur.jpg",img_blur)

