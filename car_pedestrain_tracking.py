import cv2

video = cv2.VideoCapture("test.mp4")

car_tracker = cv2.CascadeClassifier("car_detector.xml")
predestrian_detector = cv2.CascadeClassifier("predestrian_detector.xml")

while True :
    (readSuccess , frame) = video.read()
    if readSuccess :
        greyFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else :
        break
    cars = car_tracker.detectMultiScale(greyFrame)
    predestrian = predestrian_detector.detectMultiScale(greyFrame)
    
    for x,y,w,h in cars :
        cv2.rectangle(frame, (x,y),((x+w),(y+h) ), ( 0, 0, 255 ),2 )
       # cv2.rectangle(frame,(x,y-35),(w,h),(0,255,0),cv2.FILLED)
        cv2.putText(frame,"vehicle",(x,y-1),cv2.QT_FONT_NORMAL,1,(255,255,255),1)
    for x,y,w,h in predestrian :
        cv2.rectangle(frame, (x,y),((x+w),(y+h) ), (0,255,255),2 )
        cv2.putText(frame,"person",(x,y-1),cv2.QT_FONT_NORMAL,1,(255,255,255),1)
    #car_tracker = cv2.Multi
    cv2.imshow("Car_Presdestrain_Detector",frame)
    key = cv2.waitKey(1)
   
   
    if key == 113 :
        break 