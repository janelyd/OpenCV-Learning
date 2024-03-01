import cv2
import numpy as np

# canvas tanımlama:
# + 255 ile tüm değerleri beayz yaptık
canvas =np.zeros((512,512,3), dtype=np.uint8) +255

# parametreler: (canvas,metin, yazının başlicagı koordinat,yazı tipi,fontun büyüklüğü, yazı rengi,yazı tipi)
font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX




cv2.putText(canvas, "opencvv",(60,110),font1,4,(0,0,0),cv2.LINE_AA)
cv2.putText(canvas, "opencvv",(60,110),font2,1,(0,153,0),cv2.LINE_AA)
cv2.putText(canvas, "opencvv",(60,50),font3,2,(0,0,250),cv2.LINE_AA)





cv2.imshow("canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
