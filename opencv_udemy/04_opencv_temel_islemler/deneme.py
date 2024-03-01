import cv2
import numpy as np



# Görüntüyü yükle
img = cv2.imread("ornek_1.jpg")
height, width = img.shape[:2]
newheight = int(height*0.09)
newwidth = int(width*0.09)
img = cv2.resize(img, (newwidth,newheight))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Daireleri algıla
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=20, maxRadius=100)

# Eğer daireler algılandıysa, renklerini tespit et
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        # Dairenin alanını seç
        center_x, center_y = circle[0], circle[1]
        radius = circle[2]
        mask = np.zeros_like(gray)
        cv2.circle(mask, (center_x, center_y), radius, 255, -1)
        
        # Masked image'daki renk istatistiklerini hesapla
        masked_img = cv2.bitwise_and(img, img, mask=mask)
        mean_color = cv2.mean(masked_img, mask=mask)[:3]
        print("Dairenin ortalama rengi (BGR formatında):", mean_color)

        # Orta noktayı işaretle
        cv2.circle(img, (center_x, center_y), 3, (0, 255, 0), -1)
        # Daireyi çiz
        cv2.circle(img, (center_x, center_y), radius, (0, 0, 255), 2)
# BGR renk değerlerini [0, 255] aralığından [0, 1] aralığına normalleştirin
bgr_color = np.array([133.06558830046532, 179.35231553290495, 225.30556171061377]) / 255

# BGR'den [0, 1] aralığına normalleştirilmiş CIE LAB'ye dönüşüm yapın
lab_color = cv2.cvtColor(np.uint8([[bgr_color * 255]]), cv2.COLOR_BGR2LAB)[0][0]

print("CIE LAB renk değerleri:", lab_color)


# Görüntüyü göster
cv2.imshow("Daire Tespiti", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
