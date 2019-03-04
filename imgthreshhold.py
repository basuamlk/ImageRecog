import cv2
import numpy as np

img = cv2.imread('pictures\Eye\eye.jpg')
retval, threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)


# Applies threshold to show img as black and white
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2. threshold(grayscaled,12,255,cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,1)
processed_img = cv2.Canny(threshold,threshold1=100,threshold2=800)

# Erosion and Dilation
# The order here matters:
# - Dilation then erosion is called Closing, it is useful in closing small holes inside the foreground objects, or small black points on the object.
# - Erosion then dilation is called Opening, it is useful in removing noise.



cv2.imshow('original',img)
#cv2.imshow('threshold',threshold)
#cv2.imshow('threshold2',threshold2)
#cv2.imshow('gaus',gaus)
cv2.imwrite("eyeCanny_img.jpg",processed_img)
cv2.imshow('processed_img',processed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
