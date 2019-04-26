import cv2
img = cv2.imread("H:\\Github\\semester 5 projects\\py\\opencv\\MRV_20171113_23_10_39.jpg",1);
cv2.imread("MRV_20171113_23_10_39.jpg",0)
print(type(img))
print(img.shape)
cv2.imshow("test",img)#show image
cv2.waitKey(200) #timeout 

resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("resized",resized)#resize image
cv2.waitKey(0)