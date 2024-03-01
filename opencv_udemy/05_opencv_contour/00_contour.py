# convex hull --> dış bükey örtü
import cv2

img =cv2.imread("ornek_1.jpg")
height, width = img.shape[:2]
newheight = int(height*0.09)
newwidth = int(width*0.09)
img = cv2.resize(img, (newwidth,newheight))

# resmi gri tona çevirelim:
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#gri formattaki resim üzerinde thershold degiskeni:
# threshold işlemi 2 adet değişken döndürüyo
# ret önemsiz deger, onu kulllanmicaz
# cv2.threshold(gray,min deger,max deger,cv2.thbinary[ya siyah ya beyaz])
ret,thresh = cv2.threshold(gray, 127, 255,cv2.THRESH_BINARY)

# hangi değişkendeki görüntüyü thresr ediceksek o, defaul 2 deger
# aşağıdaki satırda ret,contour vs sırası fark ediyor. denedigim kombinasyonlardan dogru olanı:
contours, ret = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# son 2 parametreyi hata almamak için default olarak yazdık
# contour değişkeni içinde koordinat tutar:
# print(contours)

# drawcontour( kontorun çizilecegi resim,çizilecek kontorun listesi,-1 yani tüm konturlar çizilir,renk,kalınlık)
cv2.drawContours(img, contours,-1,(0,255,0),2)
cv2.imshow("contour deneme", img)



cv2.waitKey(0)
cv2.destroyAllWindows()