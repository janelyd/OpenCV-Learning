import cv2
import numpy as np


# ***** çember çizme******
circle = np.zeros((512,512,3),np.uint8) +255 # boş bir tuval oluşturduk
# (tuval, center, radius,color, thickness )
cv2.circle(circle,(256,256),60,(255,0,0),-1)

#**** dikdörtgen çizme****
rectangle = np.zeros((512,512,3),np.uint8) +255
# ^^^^^ dikdörtgenin çizileceği tuvali oluşturduk
cv2.rectangle(rectangle, (128,128),(384,384),color=(0,255,0),thickness=-1)
# cv2.rectangle(img, (x1, y1), (x2, y2), color=(255,0,0), thickness=2)
# x1,y1 ------
# |          |
# |          |
# |          |
# --------x2,y2


#resimleri toplamak için parametre (item1,item2):
add = cv2.add(circle, rectangle)

cv2.imshow("circle", circle)
cv2.imshow("rectangle",rectangle)

# toplamın çıktısı:
cv2.imshow("add",add)

cv2.waitKey(0)
cv2.destroyAllWindows()