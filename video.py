# -*- coding: utf-8 -*-


import cv2
import time

class prisevideo:
    def __init__(self):
        self.writer = None
        self.recording = False

    def start(self, frame):
        h, w = frame.shape[:2]
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        filename = f"event_{int(time.time())}.avi"

        self.writer = cv2.VideoWriter(filename, fourcc, 20.0, (w, h))
        self.recording = True

    def write(self, frame):
        if self.recording:
            self.writer.write(frame)

    def stop(self):
        if self.recording:
            self.writer.release()
            self.recording = False