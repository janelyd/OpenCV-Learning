import cv2


#*********************************
img = cv2.imread("ornek_1.jpg")
height, width = img.shape[:2] 
#img.shape bir NumPy dizisidir 
# ve bu dizinin ilk iki elemanı, yükseklik ve genişlik bilgisidir
new_width = int(width * 0.07)
new_height = int(height * 0.07)
img = cv2.resize(img, (new_width, new_height))
#*********************************
# görüntü şu an B,G,R modunda: r,g,b ye dönüştürmek için:
# görüntülerin renk uzayını değiştirmek için kullandıgımız fonksiyon
# cv2.cvtColor parametreler : (kaynak resim, flag(dönüşümü yapan deger))

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("img hsv", img_hsv)

cv2.imshow("img gray", img_gray)

cv2.imshow("img rgb",img_rgb)

cv2.imshow("seramik", img)

cv2.waitKey(0)
cv2.destroyAllWindows()