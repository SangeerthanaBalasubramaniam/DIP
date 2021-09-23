import sys
import cv2
import numpy

img_path = sys.argv[1]
image = cv2.imread(img_path)

h,w = image.shape[:2]

print (h,w)

start_x, end_x = 5, 8
start_y, end_y = 5, 8

condition = start_x < end_x and start_y < end_y
if condition == False:
    print('ERROR:Coordinate values are not correct')
    
crop = image[start_x:end_x, start_y:end_y]

print ('\nCropped Image Pixels:')
print ('------' * 15)
print (crop)

crop = crop + 10
print ('\nAdded 10:')
print ('----' * 5)
print (crop)

crop = crop / 10
print ('\nDivided 10: ')
print ('==='*5)
print (crop)

crop = crop * 3
print ('\n Multiplied by 3:')
print ('-----' * 5)
print (crop)
