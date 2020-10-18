from cv2 import cv2 
import numpy as np

def track(x):
       pass

lowH = 0
lowS = 0
lowV = 0
highH = 180
highS = 255
highV = 255


def set_track_pos(key):
     global lowH
     global lowS
     global lowV
     global highH
     global highS
     global highV  
     if (key == ord('b')):
         lowH = 94
         lowS = 80
         lowV = 2
         highH = 126
         highS = 255
         highV = 255
     elif (key == ord('g')):
         lowH = 25
         lowS = 52
         lowV = 72
         highH = 108
         highS = 255
         highV = 255
     elif (key == ord('o')):
         lowH = 5
         lowS = 50
         lowV = 50
         highH = 15
         highS = 255
         highV = 255  
     elif (key == ord('r')):
         lowH = 161
         lowS = 155
         lowV = 84
         highH = 179
         highS = 255
         highV = 255

     cv2.namedWindow('detection')
     cv2.createTrackbar('lowH', 'detection' , lowH, 180,track)
     cv2.createTrackbar('highH', 'detection' , highH, 180,track)
     cv2.createTrackbar('lowS', 'detection' , lowS, 255,track)
     cv2.createTrackbar('highS', 'detection' , highS, 255,track)
     cv2.createTrackbar('lowV', 'detection' , lowV, 255,track)
     cv2.createTrackbar('highV', 'detection' , highV, 255,track)


cap = cv2.VideoCapture(0)

while True:

     global lowH
     global lowS
     global lowV
     global highH
     global highS
     global highV   
     _, frame = cap.read()
     hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
     cv2.imshow('frame', frame)

          
     key = cv2.waitKey(1)
     set_track_pos(key)
        
     low_H = cv2.getTrackbarPos('lowH', 'detection')
     high_H = cv2.getTrackbarPos('highH', 'detection')
     low_S = cv2.getTrackbarPos('lowS', 'detection')
     high_S = cv2.getTrackbarPos('highS', 'detection')
     low_V = cv2.getTrackbarPos('lowV', 'detection')
     high_V = cv2.getTrackbarPos('highV', 'detection')

     mask = cv2.inRange(hsv_frame, (low_H,low_S,low_V), (high_H,high_S,high_V))
     iso = cv2.bitwise_and(frame, frame, mask=mask)
     cv2.imshow('iso',iso)
               
     key_close = cv2.waitKey(1)
     if key_close == 27:
         break        


cap.release()
cv2.destroyAllWindows()





         

        