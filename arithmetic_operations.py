import sys
import cv2
import numpy

img_path  =  sys.argv[1]
image  =  cv2.imread(img_path)

h, w = image.shape[:2]

print (h,w)

crop1 = image[1:3, 7:9] / 2
crop2 = image[10:12, 11:13 ] / 4

print ('\n===crop1===')
print (crop1)
print ('\n===crop2===')
print (crop2)

print('\n===subtracted===')
sub = crop1 - crop2
print (sub)

print ('\n===added===')
added = crop1 + crop2
print (added)
