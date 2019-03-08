import pytesseract
import cv2
import numpy as np
from PIL import Image


imgname = "3.jpg"
src_path = ""
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

def get_string(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1,1),np.uint8)
    #edges = cv2.Canny(img,100,200)
    img = cv2.dilate(img,kernel,iterations=1)
    img = cv2.erode(img,kernel,iterations=1)

    cv2.imwrite(imgname+"removed_noise.jpg",img)

    blur = cv2.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # OTSU served as a better threshold than Binary -> better for text
    
    #img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    cv2.imwrite(imgname+"thres.jpg",img)
    result = pytesseract.image_to_string(Image.open(imgname + "thres.jpg"))
    return result


print('--------text recog ---------')
print(get_string(imgname))
print('-----DONE------')
