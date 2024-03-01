import cv2
import numpy as np



img = cv2.imread("cornerdetect.jpg")


# gri formata çevirme:
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#köşelerin tutuldugu değişken: 4 adet parametre alıyor
# (değişken, max köşe sayısı,kalite değeri,köşeler arası min uzaklık)
# gray' i oldugu gibi kullanamıyoruz. floata çevirmeliyiz:
gray = np.float32(gray)
corners = cv2.goodFeaturesToTrack(gray,100, 0.01,  10)

#buldugumuz köşeleri çizmek için, corners int çevrilmeli
corners = np.int0(corners)
#tek tek bütün cornerlara çember bırakıcaz:
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img, (x,y), 3, (0,0,255), -1)

cv2.imshow("corner",img)    
cv2.waitKey(0)
cv2.destroyAllWindows()



