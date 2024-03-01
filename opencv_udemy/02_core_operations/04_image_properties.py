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


# bir görüntü üç değere sahiptir:
# yükseklik, genişlik, kanal
# bu bilgilere ulaşmak için img.shape: ()
print(img2.shape)
# img.shape'de dönen değer [height,width, channel]]
# channel degeri = 3 ise görsel renklidir
# channel değeri = 1 ise grey scaledir

print("height: {}",img.shape[0])
print("width: {} pixels", img.shape[1])
print("channel(renk): {}",img.shape[2])

#görüntünün size'ı
print(" image size: {}".format(img.size))
#image size: 144000000
# 8000*6000*3 ten geliyor
# görüntünün tipi
print(" data type: {}".format(img.dtype))



cv2.imshow("Seramik",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

