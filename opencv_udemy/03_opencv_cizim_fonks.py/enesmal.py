import cv2
import numpy as np

# Görüntüyü yükle
img = cv2.imread("ornek_1.jpg")
width, height = img.shape[:2]
new_width = int(width * 0.07)
new_height = int(height * 0.07)
img = cv2.resize(img, (new_height, new_width))

# Gri tonlamalıya dönüştür
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için bulanıklaştırma uygula
gray_blurred = cv2.medianBlur(gray, 5)

# Çember tespiti için Hough dönüşümü uygula
circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Çemberin merkezini ve yarıçapını al
        center = (i[0], i[1])
        radius = i[2]

        # Çembere çiz
        cv2.circle(img, center, radius, (0, 255, 0), 2)

# Görüntüyü göster
cv2.imshow("Cember Tespiti", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
