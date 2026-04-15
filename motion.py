# -*- coding: utf-8 -*-

import cv2

class Motion:
    def __init__(self):
        self.prev_frame = None

    def detecter(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.prev_frame is None:
            self.prev_frame = gray
            return False

        diff = cv2.absdiff(self.prev_frame, gray)
        self.prev_frame = gray

        thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
        motion_level = thresh.sum()

        return motion_level > 500000