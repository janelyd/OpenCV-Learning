import cv2
import numpy as np
import matplotlib.pyplot as plt


#*********************************
img = cv2.imread("ornek_1.jpg")
height, width = img.shape[:2]
new_width = int(width * 0.07)
new_height = int(height * 0.07)
img2 = cv2.resize(img, (new_width, new_height))


# resmim 560h,420w oldugunu görme:
print("SHAPE: {}".format(img2.shape))

(b , g , r) = cv2.split(img2)
merged = cv2.merge([b , g , r])

black = np.zeros(img2.shape[:2], dtype = "uint8")
cv2.imshow("black", black)


cv2.imshow("red", cv2.merge([black, black, r]))
cv2.imshow("blu", cv2.merge([b, black, black]))
cv2.imshow("green", cv2.merge([black, g, black]))


cv2.imshow("img2", img2)
cv2.imshow("img2-merged", merged )

cv2.imshow("img2-b", b) # blue rengini yok etme
cv2.imshow("img2-g", g) # green rengini yok etme
cv2.imshow("img2-r", r) # red rengini yok etme

cv2.waitKey(0)
cv2.destroyAllWindows()
