import cv2
import sys
path = sys.argv[1]
print ('Path:', path)
#Reads image
img = cv2.imread(path)
if img is None:
 print ("image is not valid")
h, w, c = img.shape
print (f' width: {w}')
print (f' height: {h}')
print (f' channels: {c}')
pixel = img[10, 20]
print (f'Pixel value at (10, 20): {pixel}')
if c==3:
 print (f' Blue: {pixel[0]}')
 print (f' Green: {pixel[1]}')
 print (f' Red: {pixel[2]}')
print ('Image depth (datatype):', img.dtype)
