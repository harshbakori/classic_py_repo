#capturing video
import cv2,time
video = cv2.VideoCapture(0)


check,frame = video.read()
a=1

while True:
    a=a+1
    check,frame = video.read()
    gray_img=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY) #converting to grayscale img
    cv2.imshow("capture",frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()

cv2.destroyAllWindows()
