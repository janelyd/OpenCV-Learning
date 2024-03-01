import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("ornek_1.jpg")
height,width = img.shape[:2]
new_h = int(height*0.07)
new_w = int(width*0.07)
img = cv2.resize(img,(new_w,new_h))


b,g,r =cv2.split(img)


cv2.imshow("img",img)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()