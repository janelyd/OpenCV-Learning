import cv2

cv2.namedWindow("klon")
img = cv2.imread("klon.jpg")
img = cv2.resize(img, (480,600))
# resmi göstermek için : 
cv2.imshow("klon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

