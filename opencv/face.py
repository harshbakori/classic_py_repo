import cv2
img = cv2.imread("H:\\Github\\semester 5 projects\\py\\opencv\\MRV_20171113_23_10_39.jpg",1);#img file
face_cascade = cv2.CascadeClassifier("H:\\Github\\semester 5 projects\\py\\opencv\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_alt2.xml")#xmlfile having face specifications
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) #converting to grayscale img
faces = face_cascade.detectMultiScale(gray_img,scaleFactor = 1.2,minNeighbors=5)#saving img with face ditect file 
print(type(faces))#printing type
print(faces)#printing file

for x,y,w,h in faces: #for each face in faces object
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)#make rectangal to detect

resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))#resize the image

cv2.imshow("gray",resized)#show resized image

cv2.waitKey(0)#wait untill keypress
cv2.destroyAllWindows()#delet from memory