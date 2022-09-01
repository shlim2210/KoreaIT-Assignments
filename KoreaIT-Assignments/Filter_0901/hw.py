import cv2
import sys

cap = cv2.VideoCapture(0)

if cap is None:
    print("영상을 불러올 수 없습니다.")
    sys.exit()

num = 0
while True:
    ret, frame = cap.read()

    # 1 흑백
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 2 블러처리
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 3)
    # 3 라플라시안
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    # 4 캐니
    canny = cv2.Canny(frame, 50, 50)

    filters = [frame, gray, blurred_frame, laplacian, canny]
    key = cv2.waitKey(1)

    cv2.imshow("frame", filters[num])
    #key == 13 : enter
    if key == 13:
        num += 1
        if num == 5 :
            num = 0

    # key == 27 : esc
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()