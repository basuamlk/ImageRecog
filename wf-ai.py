import numpy as np
from PIL import ImageGrab
import cv2
import time
from directionalkeys import ReleaseKey, PressKey, W,A,S,D

#finds the region of interest so that we don't have to process through all the img
def roi(img,vertices):
    #blank mask:
    mask = np.zeros_like(img) #fills in zeros from the processed_img edge matrix
    # fill the mask
    cv2.fillPoly(mask,vertices,255) #using the vertices from process_img,fills the area of the polygon
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img,mask) #does some bitwise shifting calculations
    return masked


# takes out original_img and converts the color and uses Canny edge detector algorithm
def process_img(original_img):
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)# converts img to Grayscale for easier values to work with, Gray takes '[0]' 1 value versus BRG '[255][255][255]'
    processed_img = cv2.Canny(processed_img,threshold1=200,threshold2 =300) #Canny Edge Detector using minVal and Maxval
    vertices = np.array([[10,500,],[10,300],[300,200],[500,200],[800,300],[800,500]]) #Vertices for roi
    processed_img = roi(processed_img,[vertices]) #calculates processed_img and cuts out unnecessary portions of the image
    return processed_img


#Takes image of screen at coordinates for 800x600 then deletes the windows saving memory
def main():
    last_time = time.time() # finds the current time
    while(True):
        screen = np.array(ImageGrab.grab(bbox=(0,40,800,640))) #finds location of image and captures it
        new_screen = process_img(screen) #pass screen to be converted through process_img
##        PressKey(W)
##        time.sleep(3)
##        print("up")
##        ReleaseKey(W)
        print("Loop took {} seconds".format(time.time()-last_time)) #calculates how long it took to capture an image
        last_time = time.time() #updates the time
        cv2.imshow('window',new_screen) #show the processed image
        #cv2.imshow('window2',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows() #destroy the image
            break

main()
    
