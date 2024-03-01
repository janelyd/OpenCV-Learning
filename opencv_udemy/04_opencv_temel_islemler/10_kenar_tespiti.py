import cv2

# cv2.Canny(input, min thereshold,max threshold)
#threshold eşik değerleri: 100,200 >> varsayılan

img = cv2.imread("ornek_1.jpg")
height,width = img.shape[:2]
new_h = int(height*0.07)
new_w = int(width*0.07)
img = cv2.resize(img,(new_w,new_h))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray, 100,200)


cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


