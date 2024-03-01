import cv2

cv2.namedWindow("seramik", cv2.WINDOW_NORMAL) #pencereyi boyutlandırılabilir yaptık
img = cv2.imread("ornek_1.jpg")





cv2.imshow("seramik", img)
cv2.waitKey(0)
cv2.destroyAllWindows()