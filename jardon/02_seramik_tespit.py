import cv2
import numpy as np

img = cv2.imread("ornek_2.jpg")

height, width = img.shape[:2]
new_h = int(height*0.08)
new_w = int(width*0.08)
img = cv2.resize(img, (new_w,new_h))
 



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# circle parametreleri:
# image: Dairesi algılanacak olan gri tonlamalı bir görüntü
# method: cv2.HOUGH_GRADIENT olarak belirtilirse, genellikle 21HT dönüşümü kullanılır.
# dp: 1, görüntünün orijinal çözünürlüğünde hesaplama yapar, 2 ise yarı çözünürlüğünde hesaplama yapar.
# minDist: Algılanan daireler arasındaki minimum mesafe
# param1: Canny kenar dedektörü için eşik üst sınırı.
# param2: Hesaplama sırasında kullanılan oylama eşiği. Bu değer ne kadar küçükse, daha fazla algılama olur.
# minRadius: Algılanacak en küçük daire yarıçapı.
# maxRadius: Algılanacak en büyük daire yarıçapı.
circle = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1,minDist=50,param1=200,param2=30,minRadius=20,maxRadius=100)



if circle is not None:
    # circle parametreleri x, y, r'yi int dönüştür:
    circle = np.uint16(np.around(circle))
    # x,y dairenin merkezinin koordinatları
    for (x,y,r) in circle[0, ]:
        # r piksel yarıçapında büyüklüğünde daire çiz
        cv2.circle(img, (x,y), r,(0,255,0), 2)
        # 3 pixel yarıçapında  büyüklüğünde çiz
        cv2.circle(img, (x,y), 3,(0,255,0), 2)
        print(f'Merkez Koordinatları: ({x},{y})')
        colorsB = img[y,x,0]
        colorsG = img[y,x,1]
        colorsR = img[y,x,2]
        colors = img[y,x]
        colors2 = img[y-40,x]
        colors3 = img[y-30,x]
        colors4 = img[y+30,x]
        colors5 = img[y+40,x]
        colors6 = img[y,x-40]
        colors7 = img[y,x-30]
        colors8 = img[y,x+30]
        colors9 = img[y,x+40]



        print("Red: ",colorsR)
        print("Green: ",colorsG)
        print("Blue: ",colorsB)
        print("BRG Format: ",colors)
        print("Coordinates of pixel: X: ",x,"Y: ",y)
        print(" x:",x,"y:",y, "bgr format:",colors)
        print(" x2:",x,"y:",y-40, "bgr format:",colors2)
        print(" x3:",x,"y:",y-30, "bgr format:",colors3)
        print(" x4:",x,"y:",y+30, "bgr format:",colors4)
        print(" x5:",x,"y:",y+40, "bgr format:",colors5)
        print(" x6:",x-40,"y:",y, "bgr format:",colors6)
        print(" x7:",x-30,"y:",y, "bgr format:",colors7)
        print(" x8:",x+30,"y:",y, "bgr format:",colors8)
        print(" x9:",x+40,"y:",y, "bgr format:",colors9)




cv2.imshow("daire tespiti", img)

# cv2.setMouseCallback("daire tespiti", mouseRGB)

cv2.waitKey(0)
cv2.destroyAllWindows()


