 faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.2,minNeighbors=5)#saving img with face ditect file 

    for x,y,w,h in faces: #for each face in faces object
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)#make rectangal to detect
    