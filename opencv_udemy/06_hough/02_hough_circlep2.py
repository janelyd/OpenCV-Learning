# önceki kod, görselde fazla çember buluyodu, gerekli düzenlemeleri yapalım:
import cv2
import numpy as np

img1 = cv2.imread("ornek_1.jpg")
img2 = cv2.imread("ornek_2.jpg")

height, width = img1.shape[:2]
new_h = int(height*0.07)
new_w = int(width*0.07)
img1 = cv2.resize(img1, (new_w,new_h))
img2 = cv2.resize(img2,(new_w,new_h))

gray_img_1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray_img_2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img1_blur =cv2.medianBlur(gray_img_1, 5) # 5x5 bir çekirdek kullan
img2_blur = cv2.medianBlur(gray_img_2, 5)


circles = cv2.HoughCircles(gray_img_1,cv2.HOUGH_GRADIENT,1,img1.shape[0]/10,param1 = 200, param2=10,minRadius=35,maxRadius=100)


if circles is not None:
    # Dairelerin koordinatlarını tam sayıya dönüştür ve yuvarla
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img1,(i[0],i[1]), i[2], (0,255,0),2)



cv2.imshow("ornek1", img1)



cv2.waitKey(0)
cv2.destroyAllWindows()


