# -*- coding: utf-8 -*-
"""
@author: AWOUNANG
"""
import cv2

def create_tracker(frame, bbox):
    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, bbox)
    return tracker