import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

path = "F:/seminaire/seg/iris.jfif"
image_gray =cv2.imread(path, cv2.IMREAD_GRAYSCALE)

#gaussian :
filtred_image= cv2.GaussianBlur(image_gray, (7,7), 1)
# plt.subplot(331), plt.imshow(filtred_image), plt.title('gaussiian ')

# #canny
# image_test= cv2.Canny(filtred_image, 100, 100, apertureSize=3)
# image_test1= cv2.Canny(filtred_image, 80, 100, apertureSize=7)
# image_test2= cv2.Canny(filtred_image, 80, 100, apertureSize=3)

# # # plt.subplot(332), plt.imshow(image_test), plt.title('canny')
# # # plt.subplot(333), plt.imshow(image_test), plt.title('canny80-100')
# # # plt.subplot(334), plt.imshow(image_test), plt.title('canny80-100, aper size =7')

# #hough
# circles= cv2.HoughCircles(image_test2, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=50, minRadius=0, maxRadius=0)

# #draw circles :
# if circles is not None:

#     #convertir a et b et r to integres :
#     circles=np.uint16(np.around(circles))

#     for pt in circles [0,:]:
#         a, b , r = pt[0], pt[1], pt[2]

#         #draw circle
#         cv2.circle(image_gray, center=(a,b), radius= r, color= (255,255,0), thickness= 2)
#         cv2.circle(image_gray, (a, b), 1, (0, 0, 255), 3)
#         plt.imshow(image_gray)
#         plt.show()



# circles = np.round(circles[0, :]).astype("int")

# for (x, y, r) in circles:
# 		# draw the circle in the output image, then draw a rectangle
# 		# corresponding to the center of the circle
# 		cv2.circle(output, (x, y), r, (0, 255, 0), 2)
# 		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

# cv2.imshow('detected circles',output)
# cv2.waitKey(0)


#detcter momo :
#canny
image_test=cv2.Canny(filtred_image, 80,100, apertureSize= 3)

#hough cirlce :
circles = cv2.HoughCircles(image_test,cv2.HOUGH_GRADIENT, 1, 20)
if circles is not None:

    #convertir a et b et r to integres :
    circles=np.uint16(np.around(circles))
    for pt in circles [0,:]:
        a, b , r = pt[0], pt[1], pt[2]
        cv2.circle(image_gray, (a,b), r, (255,0,0), thickness=4)


		
image_test = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
image_test = cv2.GaussianBlur(image_test, (7, 7), 1)
image_test = cv2.Canny(image_test, 100, 120, apertureSize=3)

circles = cv2.HoughCircles(image_test,cv2.HOUGH_GRADIENT,1.3,800,
                            param1=50,param2=20,minRadius=1,maxRadius=40)

circles=np.uint16(np.around(circles))

for pt in circles [0,:]:
        a, b , r = pt[0], pt[1], pt[2]
        cv2.circle(image_gray, (a,b), r, (255,0,0), thickness=2)


plt.imshow(image_gray)
plt.show()
