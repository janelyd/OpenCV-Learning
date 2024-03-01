import cv2
import numpy as np

img = cv2.imread("ornek_1.jpg")
height, width = img.shape[:2]
new_height = int(height*0.07)
new_width = int(width*0.07)
img = cv2.resize(img, (new_width,new_height))

blur = cv2.blur(img,(1000,1000))

bit_and = cv2.bitwise_and(img,blur)
bit_or = cv2.bitwise_or(img,blur)
bit_xor = cv2.bitwise_xor(img,blur)
bit_not = cv2.bitwise_not(img,blur)
bit_not2 = cv2.bitwise_not(img,blur)


cv2.imshow("bitwise not ", bit_not)

cv2.imshow("bitwise not2 ", bit_not2)

cv2.imshow("bitwise xor ", bit_xor)

cv2.imshow("bitwise or ", bit_or)

cv2.imshow("bitwise and ", bit_and)

cv2.imshow("blur ", blur)

cv2.imshow("ornek ", img)

cv2.waitKey(0)
cv2.destroyAllWindows()