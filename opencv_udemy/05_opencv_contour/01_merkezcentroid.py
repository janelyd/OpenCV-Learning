import cv2
img = cv2.imread("ornek_1.jpg")
height, width = img.shape[:2]
newheight = int(height*0.09)
newwidth = int(width*0.09)
img = cv2.resize(img, (newwidth,newheight))
 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

Moments= cv2.moments(thresh)
#**********agırlık merkezi bulma:
X =  int(Moments["m10"]/Moments["m00"])
Y =  int(Moments["m01"]/Moments["m00"])

cv2.circle(img,(X,Y),5,(255,255,0),-1)

cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()