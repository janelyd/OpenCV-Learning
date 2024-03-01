# görüntüleri belirli yogunluklarda birbiri üstüne ekleme
# ağırlık toplamın matematiksel gösterimi:
# f(x,y)= x*a + y*b +c ----> x degerini a yogunluguyla, y degerini b yogunlugu ile, c sabit
import cv2
import numpy as np

circle = np.zeros((512,512,3),np.uint8)+255
rectangle = np.zeros((512,512,3),np.uint8)+255

# sourceimage, (x coordinate, y coordinate), radius, color and thickness.
cv2.circle(circle, (256,256),50,(0,255,0),-1)
#(img, (x1, y1), (x2, y2), color=(255,0,0), thickness=2)
cv2.rectangle(rectangle, (128,128),(384,384),(0,0,0),-1)

#dst: ağırlıklı eklenmiş foto,
# parametre (ilk resim, ilk resmin yüzde kaç yoğunlukta eklenceği,2. resim,2. resmin kelencegi yogunluk, sabit sayı(c))
dst = cv2.addWeighted(circle, 0.7 ,rectangle, 0.3,0)

cv2.imshow("ağırlıklı toplam", dst)

cv2.imshow("circle",circle)
cv2.imshow("rectangle",rectangle)

cv2.waitKey(0)
cv2.destroyAllWindows()
