# -*- coding: utf-8 -*-
"""
Created on Wed Apr 03 19:20:00 2026

@author: AWOUNANG
"""

import cv2

def get_camera():
    return cv2.VideoCapture(0, cv2.CAP_DSHOW)