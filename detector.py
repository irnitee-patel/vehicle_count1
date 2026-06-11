from ultralytics import YOLO

class VehicleDetector:

    def __init__(self):

        self.model = YOLO("yolov8n.pt")

        self.vehicle_classes = [
            2,  # car
            3,  # motorcycle
            5,  # bus
            7   # truck
        ]

    def detect(self, frame):

        results = self.model(frame, verbose=False)

        detections = []

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                if cls in self.vehicle_classes:

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    w = x2 - x1
                    h = y2 - y1

                    detections.append(
                        (x1, y1, w, h)
                    )

        return detections
