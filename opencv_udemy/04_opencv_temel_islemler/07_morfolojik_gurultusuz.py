import cv2
import numpy as np

img = cv2.imread("ornek_1.jpg")
height,width = img.shape[:2]
new_h = int(height*0.07)
new_w = int(width*0.07)
img = cv2.resize(img,(new_w,new_h))
# bir fonksiyon ile resmi erosyona ugratıcaz:
# cv2.erode(erosyana ugricak resim, belli bi dizey[kernel], kaç kere tekrarlancagı)
kernel = np.zeros((0,0),np.uint8) # birlerden oluşan matris
# bu matrisi resim üzerine getirerek bozdurucaz
erosion = cv2.erode(img, kernel, iterations= 5)


#delation yöntemi:

dilation = cv2.dilate(img, kernel, iterations=1)

# dilation yöntemi ile oluşşan resimdeki gürültüyü kaldırma
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
# opening gürültü silme, closing siyah noktaları silme
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

cv2.imshow("closşng",closing)
cv2.imshow("opening",opening)
cv2.imshow("erozyon",erosion)
cv2.imshow("dilate",dilation)


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()