import cv2
import numpy as np
from colour.models import RGB_to_XYZ, XYZ_to_Lab


img = cv2.imread("ornek_2.jpg")

height, width = img.shape[:2]
new_h = int(height*0.08)
new_w = int(width*0.08)
img = cv2.resize(img, (new_w,new_h))
 



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


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
        colors1 = img[y,x]
        colors2 = img[y-40,x]
        colors3 = img[y-30,x]
        colors4 = img[y+30,x]
        colors5 = img[y+40,x]
        colors6 = img[y,x-40]
        colors7 = img[y,x-30]
        colors8 = img[y,x+30]
        colors9 = img[y,x+40]

# İlgili piksellerin renk değerlerini içerecek boş listeler oluşturun
all_colorsB = []
all_colorsG = []
all_colorsR = []

# Her bir pikselin renk değerlerini listelere ekleyin
all_colorsB.extend([colors1[0], colors2[0], colors3[0], colors4[0], colors5[0], colors6[0], colors7[0], colors8[0], colors9[0]])
all_colorsG.extend([colors1[1], colors2[1], colors3[1], colors4[1], colors5[1], colors6[1], colors7[1], colors8[1], colors9[1]])
all_colorsR.extend([colors1[2], colors2[2], colors3[2], colors4[2], colors5[2], colors6[2], colors7[2], colors8[2], colors9[2]])

# len, colorsB içinde kaç eleman oldugunu verir
# Renk değerlerinin ortalamasını hesaplayın
averageB = sum(all_colorsB) / len(all_colorsB)
averageG = sum(all_colorsG) / len(all_colorsG)
averageR = sum(all_colorsR) / len(all_colorsR)


print("Blue Average:", averageB)
print("Green Average:", averageG)
print("Red Average:", averageR)

# RGB değerlerini 0-1 aralığına normalize et
B = averageB / 255
R = averageR / 255
G = averageG / 255

# BGR'den XYZ'ye dönüşüm için RGB dizisini oluştur
RGB = np.array([B, G, R])

# RGB'den XYZ'ye dönüşüm
XYZ = RGB_to_XYZ(RGB,colourspace='sRGB')

# XYZ'den CIE LAB'ye dönüşüm
Lab = XYZ_to_Lab(XYZ)

# CIE LAB formatında L*, a* ve b* değerlerini yazdır
print("CIE LAB L*: ", Lab[0])
print("CIE LAB a*: ", Lab[1])
print("CIE LAB b*: ", Lab[2])

cv2.imshow("daire tespiti", img)


cv2.waitKey(0)
cv2.destroyAllWindows()