
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


#Converting BGR in RGB image (swaps B and R channels)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imwrite("swap.jpg",img_rgb)

