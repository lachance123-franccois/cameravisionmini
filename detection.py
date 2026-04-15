# -*- coding: utf-8 -*-
from ultralytics import YOLO

class Detectervisag:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detecter(self, frame):
        resultats = self.model(frame, verbose=False)
        detections = []

        for r in resultats:
            for box in r.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])

                # class 0 = person
                if cls == 0 and conf > 0.5:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    detections.append((x1, y1, x2, y2, conf))

        return detections