import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 


image = cv.imread('iris.jfif')
image_gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  


def preprocessing(image_gray, ksize, thresh, maxval, shape, shape2 ):
    filtred_image = cv.GaussianBlur(image_gray, ksize, 0)
    ret,th1 = cv.threshold(filtred_image,thresh,maxval,cv.THRESH_BINARY)
    kernel1 = np.ones(shape,np.uint8)
    opening = cv.morphologyEx(th1, cv.MORPH_OPEN, kernel1)
    kernel2 = np.ones(shape2,np.uint8)
    opening1 = cv.morphologyEx(th1, cv.MORPH_OPEN, kernel2)
    return opening, opening1, th1


finale1, finale2, finale3= preprocessing(image_gray, ksize=(3,3), thresh=90, maxval=255, shape=(9,9), shape2=(16, 16))

plt.subplot(311),plt.imshow(finale3),plt.title('th1')
plt.subplot(312),plt.imshow(finale1),plt.title('opening')
plt.subplot(313),plt.imshow(finale2),plt.title('opening1')
plt.show()