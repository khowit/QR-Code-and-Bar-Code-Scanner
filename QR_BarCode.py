import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        

while True:
    success, frame = cap.read()
    for barcode in decode(frame):
        print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            print("Authoried")

        else:
            print("Un-Authoried")

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(frame,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(frame,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
    
    cv2.imshow("Output", frame)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break 

cap.release()
cv2.destroyAllWindows()
