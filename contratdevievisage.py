# -*- coding: utf-8 -*-
"""
Created on  2025

@author: AWOUNANG
"""

import cv2
from detection import Detectervisag
from motion import Motion
from video import prisevideo

cap = cv2.VideoCapture(0)

detection =Detectervisag()
motion = Motion()
vid = prisevideo()

record = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    people = detection.detecter(frame)

    motion_detecte = motion.detecter(frame)

    if len(people) > 0 or motion_detecte:
        if not record:
            vid.start(frame)
            recording = True

        vid.write(frame)

    else:
        if recording:
            vid.stop()
            recording = False

    
    for (x1, y1, x2, y2, conf) in people:
    
        # marge de reduction (plus grand = rectangle plus petit)
        marge_x = int((x2 - x1) * 0.10)
        marge_y = int((y2 - y1) * 0.10)
    
        x1_r = x1 + 2*marge_x
        y1_r = y1 + 2*marge_y
        x2_r = x2 - 2*marge_x
        y2_r = y2 - 2*marge_y
    
        cv2.rectangle(frame, (x1_r, y1_r), (x2_r, y2_r), (255, 255, 255), 2)
    
        cv2.putText(frame, "lachance", (x1_r, y1_r - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        
        
    cv2.imshow("contratdevie", frame)

    if cv2.waitKey(1) & 0xFF == 13:
        break

cap.release()
cv2.destroyAllWindows()