#motion ditector
import cv2,time


first_frame = None
video = cv2.VideoCapture(0)
a=1
while True:
    a=a+1
    check,frame = video.read()#read frame 
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)#convert to grayscale
    gray = cv2.GaussianBlur(gray,(21,21),0)#convert to gaussianblur

    if first_frame is None:
        first_frame = gray  #if first frame is null fill it with this frame
        continue

    delta_frame = cv2.absdiff(first_frame,gray) #define this frame
    threas_delta = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]#convert with thresold
    threas_delta = cv2.dilate(threas_delta,None,iterations=0)#calculate the difference

    
    (cnts,_) = cv2.findContours(threas_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#set the difference

    for contour in cnts: #count the area of change
        if cv2.contourArea(contour) < 1000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)#make the rectangle around the changes
        cv2.rectangle(frame , (x,y),(x+w,y+h),(0,255,0),3)#set rectangle

    
    cv2.imshow("frame",frame)
    #v2.imshow("gray",gray)
   #cv2.imshow("capture",delta_frame)
    #v2.imshow("thres",threas_delta)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break
print(a)
video.release()

cv2.destroyAllWindows()