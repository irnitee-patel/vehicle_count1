class VehicleCounter:

    def __init__(self, line_y):

        self.line_y = line_y

        self.count = 0

        self.detected_centers = []

    def update(self, detections):

        for (x, y, w, h) in detections:

            cx = x + w // 2
            cy = y + h // 2

            if abs(cy - self.line_y) < 10:

                if (cx, cy) not in self.detected_centers:

                    self.detected_centers.append((cx, cy))

                    self.count += 1

        return self.count