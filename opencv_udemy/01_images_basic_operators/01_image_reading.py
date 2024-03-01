# resmin matematiksel, piksel ve renk değerlerini okuma
import cv2

# okudugumuz şeyi hafızaya kaydetmek için değişken atamamız lazım
# cv2.imread() fonksiyonu ile resmin matematiksel değerini okuyup img değişkenine eşitle:

img = cv2.imread("klon.jpg")
# veya ---- img = cv2.imread("D:\opencv_udemy\klon1.jpg")


print(img)
# **başta none çıktısı gelmesinin sebebi : klon.jog 01 içindeydi
# ---RESMİ GRİ TONDA OKUMAK İÇİN---

# img = cv2.imread("klon.jpg",cv2.IMREAD_GRAYSCALE)
# print(img)


cv2.namedWindow("image",cv2.WINDOW_NORMAL) # pencerenin boyutlandırmasını manuel ayarlamak için
# resmi kaydetmek için -->
cv2.imwrite("klon1.jpg", img) # kaydediceğimiz resmin bulundugu değişken


cv2.imshow("image",img) # --> görseli açma
cv2.waitKey(0) #--> ekranda bekleme süresi ayarlama
cv2.destroyAllWindows() # hatalardan kurtulmak için her kodun sonuna yazılması gerekiyormuş


