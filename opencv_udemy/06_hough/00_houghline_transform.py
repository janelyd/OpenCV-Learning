# bu kodda for kısmında bir sıkıntı var çözemedim

import cv2
import numpy as np

img = cv2.imread("ornek_1h.jpg")
height, width = img.shape[:2]
new_h = int(height*0.07)
new_w = int(width*0.07)
img = cv2.resize(img,(new_w,new_h))

grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(grayimg,170,750)

# çizgi tespiti houghLines: (köşeleri bulunmuş resim,ro ve teta degerleri, threshold degeri)
lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)

#????????????????????????????????????????????
# for döngüsü olmadan okuyamayız:
if lines is not None:
    # Her bir çizgi segmenti için döngü
    for line in lines:
        x1, y1, x2, y2 = line[0]  # Her çizgi segmentinin koordinatlarını al
        # Alınan koordinatları kullanarak çizgiyi çiz
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)



cv2.imshow("img",img)
cv2.imshow("gray",grayimg)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()






