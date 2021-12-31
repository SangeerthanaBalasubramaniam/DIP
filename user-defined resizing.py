import numpy as np
import cv2
import sys

def resize(src, wfac, hfac):
  h, w, c = src.shape
  B = src[:,:,0]
  G = src[:,:,1]
  R = src[:,:,2]
  B1 = B[1::wfac,1::hfac]
  G1 = G[1::wfac,1::hfac]
  R1 = R[1::wfac,1::hfac]
  out = np.zeros((h//wfac, w//hfac, c),np.uint8)
  out[:,:,0] = B1
  out[:,:,1] = G1
  out[:,:,2] = R1
  return out 

path = sys.argv[1]
img = cv2.imread(path)
print("Input image shape:", img.shape)

new_image = resize(img, 2, 2)

print("Resized image shape:", new_image.shape)
cv2.imwrite("output.jpg",new_image)
