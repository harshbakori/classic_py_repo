#capturing video
import cv2,time
face_cascade = cv2.CascadeClassifier("D:\\Github\\semester 5 projects\\py\\opencv\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_alt2.xml")#xmlfile having face specifications
#face_cascade = cv2.CascadeClassifier("/media/harsh/Dead Zone {-_-}/Github/semester 5 projects/py/opencv/opencv-master/data/haarcascades/haarcascade_frontalface_alt.xml")#xmlfile having face specifications

video = cv2.VideoCapture(0)


check,frame = video.read()
a=1

while True:
    a=a+1
    check,frame = video.read()
    gray_img=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY) #converting to grayscale img
    
    faces = face_cascade.detectMultiScale(gray_img,scaleFactor = 1.2,minNeighbors=5) #saving img with face ditect file 
    for x,y,w,h in faces: #for each face in faces object
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)#make rectangal to detect
       # print(x,x+w,y+h,y)
    
    cv2.imshow("capture",frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()

cv2.destroyAllWindows()
