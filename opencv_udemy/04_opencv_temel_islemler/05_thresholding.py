import cv2
import numpy as np

img = cv2.imread("ornek_1.jpg",0)
height, width = img.shape[:2]
new_height = int(height*0.07)
new_width = int(width*0.07)
img = cv2.resize(img,(new_width,new_height))

# thresholding: öbeklendirme
# iki değişken kullanmalıyız
# return: ret, th1: ilk threshold yöntemi
# (hangi resme uygulancagı, threshold yapılcak aralık: min deger, max deger)
ret, th1 = cv2.threshold(img,155,600,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,111,2)
th3 =cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,687,2)

cv2.imshow("th3",th3)
cv2.imshow("th2",th2)
cv2.imshow("threshold",th1)

cv2.imshow("seramik",img)

cv2.waitKey(0)
cv2.destroyAllWindows()