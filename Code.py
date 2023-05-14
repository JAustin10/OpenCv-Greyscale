#import cv2 module
import cv2 as cv
#import numpy module
import numpy as np
#read the image
img=cv.imread('/Users/joshna/img.jpg')
#change the color scale to grey
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#show the resultant image
cv.imshow("gray_image",gray_img)
cv.waitKey(0)
cv.destroyAllWindows()