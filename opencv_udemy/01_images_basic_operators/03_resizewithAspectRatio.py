import cv2

# inter = cv2.inter_area : resmi yeniden boyutlandırırken çakışma&interpolasyon olmasın
def resizewithAspectRatio(img, width=None, height=None, inter = cv2.INTER_AREA):
    dimension = None
    (h,w) = img.shape[:2]