import cv2

class VehicleDetector:

    def __init__(self):
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2(
            history=100,
            varThreshold=40
        )

    def detect(self, frame):

        mask = self.bg_subtractor.apply(frame)

        _, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (5, 5)
        )

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_CLOSE,
            kernel
        )

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        detections = []

        for contour in contours:

            area = cv2.contourArea(contour)

            if area > 800:

                x, y, w, h = cv2.boundingRect(contour)

                detections.append((x, y, w, h))

        return detections