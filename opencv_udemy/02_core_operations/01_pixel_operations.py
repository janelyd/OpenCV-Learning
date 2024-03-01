import cv2
import numpy as np

img = cv2.imread("ornek_1.jpg")
# resmin boş olup olmadıgı kontrolü: matris dönecek
print(img) # matrisi döndürecek, resmi açmayacak


# 0,0 daki piksel değerini px atadık, istenen koordinattaki renk degerini okuduk

# px = img[10,10]
# print(px)

# (b, g, r) tuple'ı: 50,0 koordinatındaki renk degerini tutucak
# ayrı ayrı piksel degerlerine ulaşma:
(b, g, r) = img[50,30]
print("(0,0) - red: {}, green: {}, blue: {}".format(r,g,b))

# renkler bgr/rgb karışımından oluşmuşsa 0dan 255e kadar deger alırlar

# sadece blue degerine ulaşmak için 100,100deki blue degeri:
# ---------pixel degerine ulaşma-1 -----------
# blue, 0ıncı indeks
# green 1inci indeks
# red 2nci indeks
blue = img[100,100,0]
print(img[100,100,0])
print(blue) # ikisi de aynı sonucu verir

red = img[100,100,2]
green = img[100,100,1]
print(red)
print(green)



#----------------------------------------
# resmin orijinalinde, [100,100] deki renk degeri: [151,155,158] idi
# seçilen matristeki BGR degerini değiştirebiliriz:
print("before: ", img[100,100])
# [151,155,158] --> [0,0,0]
img[100,100]= [0,0,0] # siyah yaptık
print("After: ", img[100,100])


# ---------pixel degerine ulaşma-2 -----------
img.item(10,10,2) # [10,10]daki red degerine erişme
print("Red value (before)on 10,10: ", img.item(10,10,2))
# buradaki red'in değerini değiştirme:
img.itemset((10,10,2),0)
print("Red value(after) on 10,10: ", img.item(10,10,2))
