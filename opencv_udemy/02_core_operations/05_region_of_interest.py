import cv2
import numpy as np
import matplotlib.pyplot as plt


#*********************************
#resmimin normal boyutu 8000x6000
#resmi normal boyutunun yüzde 7si olarak görme:

img = cv2.imread("ornek_1.jpg")
height, width = img.shape[:2]
new_width = int(width * 0.07)
new_height = int(height * 0.07)
img2 = cv2.resize(img, (new_width, new_height))


# resmim 560h,420w oldugunu görme:
print("SHAPE: {}".format(img2.shape))

roi = img2[220:320,135:260] # seçtiğimiz/kırptıgımız kısım
img2[100:200,50:175] = roi
# kırptıgımız kısmı başka bi yere yapıştırma:(atama ile)


cv2.imshow("roi", roi)
cv2.imshow("roi", img2)



cv2.waitKey(0)
cv2.destroyAllWindows()
