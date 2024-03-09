import cv2
import numpy as np
import sqlite3 as sql

img = cv2.imread("ornek_1.jpg")

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
        neighbor_pixels = [
    (0, 0),  # Kendi pikselimiz
    (0, -5), (0, 5), (-5, 0), (5, 0),  # 5 piksel aralıklarla
    (0, -10), (0, 10), (-10, 0), (10, 0),  # 10 piksel aralıklarla
    (0, -15), (0, 15), (-15, 0), (15, 0),  # 15 piksel aralıklarla
    (0, -20), (0, 20), (-20, 0), (20, 0),  # 20 piksel aralıklarla
    (0, -25), (0, 25), (-25, 0), (25, 0),  # 25 piksel aralıklarla
    (0, -30), (0, 30), (-30, 0), (30, 0),  # 30 piksel aralıklarla
    (0, -35), (0, 35), (-35, 0), (35, 0),  # 35 piksel aralıklarla
    (0, -40), (0, 40), (-40, 0), (40, 0),  # 40 piksel aralıklarla
]


        colors = []
        for dx, dy in neighbor_pixels:
            colors.append(img[y + dy, x + dx])

for i, (dx, dy) in enumerate(neighbor_pixels):
    pixel_x, pixel_y = x + dx, y + dy
    pixel_color = img[pixel_y, pixel_x]

    print(f"Coordinates of pixel {i + 1}: X: {pixel_x}, Y: {pixel_y}")
    print("BGR Format:", pixel_color)
    print("Red:", pixel_color[2])
    print("Green:", pixel_color[1])
    print("Blue:", pixel_color[0])






cv2.imshow("daire tespiti", img)

# cv2.setMouseCallback("daire tespiti", mouseRGB)

cv2.waitKey(0)
cv2.destroyAllWindows()


