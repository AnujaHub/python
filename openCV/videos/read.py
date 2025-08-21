import cv2 as cv

# img = cv.imread('photos/cat.jpeg') 

# # Reads the image file cat.jpeg from the photos folder.
# # Loads it into the variable img as a NumPy array (matrix of pixel values).

# cv.imshow('cat' , img) 

# capture = cv.VideoCapture(0) 
# provide 0 as an argument when accessing webcam also 
# make sure webcam is assign 0 if multiple cam exists.

capture = cv.VideoCapture('test01.mp4') 

while True:
    isTrue , frame = capture.read()
    # video is sent frame by frame 
    # each farme is checked by a boolean - 
    # whether it was succesfully read or not
    
    cv.imshow('video',frame) #display video

    # to stop video from playing infinitely 
   # wait 20ms for a key press, get ASCII value
   # mask with 0xFF to handle system differences
   # if pressed key is 'd', exit loop
 
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release() 
cv.destroyAllWindows() 
  

 


