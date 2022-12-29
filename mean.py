import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from PIL import Image, ImageFilter
from conv import convolved_2d
import skimage.feature
import skimage.viewer



###reading the image: 

image = cv2.imread("image.JPG")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #to read correctly yth ecolors 

#mean filter : kyen f opencv klch heehe
av3 = cv2.blur(image, (3, 3))
av5 = cv2.blur(image, (25, 25))
plt.figure().set_size_inches(25,25)
plt.subplot(331),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(332),plt.imshow(av3),plt.title('Averaging - 3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(333),plt.imshow(av5),plt.title('Averaging - 25x25')
plt.xticks([]), plt.yticks([])


###Median filter : 
median= cv2.medianBlur(image,9)

#compare = np.concatenate((image, median), axis=1)
plt.subplot(334),plt.imshow(median),plt.title(' median 25')


#gaussian
gaussian =  cv2.GaussianBlur(image,(25,25),0)

plt.subplot(335),plt.imshow(gaussian),plt.title(' gaussian')


#edge detection :

edge = cv2.Canny(image=image,threshold1=1,threshold2=50,)

plt.subplot(336),plt.imshow(edge),plt.title(' edge')



#max filter 

image= Image.open("image.JPG")

filterApplied = image.filter(ImageFilter.MaxFilter);

plt.subplot(337),plt.imshow(filterApplied),plt.title('max')


#histogramme 
image = cv2.imread('image.JPG')
hista = plt.subplot(338).hist(image.ravel(), bins = 256)
plt.title('histogramme')

plt.show()