import cv2 as cv

img = cv.imread('photos/cat.jpeg') 

# Reads the image file cat.jpeg from the photos folder.
# Loads it into the variable img as a NumPy array (matrix of pixel values).

cv.imshow('cat' , img) 


cv.waitKey(0) #delay