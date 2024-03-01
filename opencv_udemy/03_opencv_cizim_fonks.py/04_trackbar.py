import cv2
import numpy as np

#boş fonksiyon:
def nothing(x):
    pass

# canvas oluşturmak için np.zeros fonksiyonu(boyut ve channel)
img = np.zeros((512,512,3),np.uint8)

# oluşturdugumuz pencereye ad vericez ki diger pencereyle aynı olsun:
cv2.namedWindow("image")# pencereye ad verdik


# parametre: (kızagın adı, kızagın yerleşecegi pencerenin adı, kızagın başlangı, kızagın son degeri)

cv2.createTrackbar("Red","image", 0 ,255,nothing) # fonksiyonun hatasız çalışması için nothing fonksiyonu girmek gerek
cv2.createTrackbar("Green","image", 0 ,255,nothing)
cv2.createTrackbar("Blue","image", 0 ,255,nothing)
switch = "0: OFF, 1: ON"
cv2.createTrackbar(switch,"image", 0 ,1,nothing)


# buraya kadar trackbar degeri okuduk. bu degerleri pencereye yansıtmak için:

#pencerenin sürekli yenilenmesi için while döngüsü:
while True:
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 
    # 1 milisaniyede pencere yenilenecek, q ya bastıgımızda kapanacak

    # kızakların konumunu alıp degiskende saklama
    red = cv2.getTrackbarPos("Red","image")
    green = cv2.getTrackbarPos("Green","image")
    blue = cv2.getTrackbarPos("Blue","image")
    
    s = cv2.getTrackbarPos(switch,"image")


    # swicth için fonksiyon tanımlama:
    if s == 0:
        img[:] == [0,0,0] # swicth 0 iken tüm değerler 0 olup siyah ekran olsun
    if s == 1:
        img[:] =[blue,green,red]



    # aldıgımız bu degerleri, rengin değişmesi için pencereye göndericez:
  
 
cv2.destroyAllWindows()



cv2.waitKey(0)
cv2.destroyAllWindows()