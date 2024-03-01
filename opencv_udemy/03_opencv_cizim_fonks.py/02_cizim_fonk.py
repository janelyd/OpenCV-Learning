import cv2
import numpy as np

# + 255 ile tüm değerleri beayz yaptık
canvas =np.zeros((512,512,3), dtype=np.uint8) +255

#------- basit çizgi çizme
# ( çizim yapacagımız tuval(canvas), çizginin başlayacağı piksel, çizginin bitiş noktası,çizgi rengi(bgr), kalınlık)
cv2.line(canvas,(50,50),(512,512),(255,0,0), thickness=5 )
cv2.line(canvas,(100,50),(200,250),(0,0,255), thickness=5 )

# -------dikdörtgen çizme
# sırasıyla parametreler:
#(çizim yapılacak yer, sol üst köşe, sağ alt köşe,renk,kalınlık)
cv2.rectangle(canvas,(100,100),(200,250), (97, 95, 232),thickness=-1)
# dikdörtenin içini dolu yapmak istiyorsak thickness= -1 olacak


#-----------ÇEMBER ÇİZME
# çember parametreleri: (canvas, merkez, yarıçap, renk, kalınlık)
cv2.circle(canvas, (300,300), 100,(222,150,150), thickness=15)


# üçgen çizmek için ayrı bir cv2 fonksiyonu yok, option olarak

p1 = (100,200)
p2 = (50,50)
p3 = (300,100)
# ilk çizgi için: (canvas,ilk nokta,son nokta,renk, kalınlık)
cv2.line(canvas, p1,p2,(0,0,0),4)
cv2.line(canvas, p2,p3,(0,0,0),4)
cv2.line(canvas, p1,p3,(0,0,0),4)

# YAMUK- BEŞGEN VS ÇİZMEK İÇİN
#önce numpy dizisi oluşturmalıyız: çizim fonksiyonları videosuu!!!
# points = np.array
# cv2.polylines([[[110,200],[330,200],[290,220],[220,250]]],np.int32)


cv2.imshow("canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()

