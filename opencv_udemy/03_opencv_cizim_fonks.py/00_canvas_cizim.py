import cv2
import numpy as np

# canvas, yani çizim yapıcagımız yer
# belli bir büyüklükte siyah ekran oluşturma
canvas = np.zeros((512,512,3),dtype=np.uint8)  + 255 # çizim yaptıgımızda kullandıgımız veri tipi uint8
# kanal verisi 3 olsun ki renkli çizimler yapabilelim


cv2.imshow(" canvas ",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()