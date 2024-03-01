import cv2
# aş. fonksiyon içine 4 adet değişken girildi,
# ilk değişken resmin tutuldugu değişken: img
# 2. ve 3. değişken: width(en), height [ilk değeri none, fonksiyonu kullanırken değerleri giricez]
# inter değişkenine inter = cv2.inter_area atadık. 
# cv2.INTER_AREA: Piksel alanı enterpolasyonu. Piksel 
# değerleri alan oranına göre yeniden örneklendirilir.

def resizewithOriginalRatio(img, width = None, height = None, inter = cv2.INTER_AREA):
    # resmin yeni boyutunu dimension olarak tanımladık.
    dimension = None
    (h,w) = img.shape[:2] #en başından 2.ye kadar olan resmin boyut degerleri

    # fonksiyonun içine en ve boy degeri girilmezse resmin aynısını döndür
    if width is None and height is None:
        return img
    # eger kullanıcı sadece width değerini girmez ise:
    # girdiği boy değerine uygun boyut hesabı yapacagız,
    if width is None:
        # boyut hesabı için r:
        r = height / float(h)
        # height: kullanıcının verdiği boy değeri
        # h : resmin boy degeri
        dimension = (int(w*r), height)
    # eger kullanıcı sadece height degerini verirse
    else:
        r = width / float(w)
        dimension = (width,int(r*h))

    return cv2.resize(img, dimension, interpolation= inter)
    # return içindeki degerlerin açıklaması:
    # img: Boyutlandırılacak olan orijinal görüntü
    # dimension: Yeniden boyutlandırılmış görüntünün hedef
    # boyutları. Bu, genişlik ve yükseklik değerlerini
    # içeren bir tuple'dır
    # interpolation: Yeniden boyutlandırma sırasında 
    # kullanılacak enterpolasyon yöntemini belirler

img = cv2.imread("ornek_1.jpg")
# yeniden boyutlandırdıgım görselin atandıgı img1 degiskeni:
img1 = resizewithOriginalRatio(img, width = None, height = 600, inter = cv2.INTER_AREA)


cv2.imshow("orijinal", img)
cv2.imshow("resized", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()