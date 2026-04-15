# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:35:05 2026

@author: AWOUNANG
"""

import cv2
import mediapipe as mp

class suivi_main:
    def __init__(self, max_hands=1, detection_conf=0.7, tracking_conf=0.7):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_conf,
            min_tracking_confidence=tracking_conf
        )
        self.mp_draw = mp.solutions.drawing_utils

    def rechech(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultats = self.hands.process(rgb)

        liste_repere = []

        if resultats.multi_hand_landmarks:
            for handLms in resultats.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame,
                    handLms,
                    self.mp_hands.HAND_CONNECTIONS
                )

                h, w, _ = frame.shape
                landmarks = []

                for id, lm in enumerate(handLms.landmark):
                    x, y = int(lm.x * w), int(lm.y * h)
                    landmarks.append((id, x, y))

                liste_repere.append(landmarks)

        return frame,liste_repere