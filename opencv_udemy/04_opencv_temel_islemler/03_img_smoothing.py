import cv2
import numpy as np

img_filter = cv2.imread("ornek_1.jpg")
height, width = img_filter.shape[:2]
new_height = int(height*0.07)
new_width = int(width*0.07)
img_filter = cv2.resize(img_filter, (new_width,new_height))

img_gurultulu = cv2.imread("gurultuluresim.jpg")

# resmi blurlama (yogunluk)
blur = cv2.blur(img_filter,(10,10))

# cv2.border_default ----> sınır bilgisi varsayılan olsun
blur_gaussian = cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT)


# gürültülü resim:
blur_median = cv2.medianBlur(img_gurultulu,111)
# pozitif tek sayılar vermeliyiz



cv2.imshow("gurultulu resim",img_gurultulu)


cv2.imshow("ornek1", img_filter)
cv2.imshow("blur",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
