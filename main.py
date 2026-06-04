import cv2
import time

from detector import VehicleDetector
from counter import VehicleCounter
from utils import save_report

VIDEO_PATH = "input/traffic.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 30

print("Video Opened Successfully")
print("Width:", width)
print("Height:", height)
print("FPS:", fps)

output_video = cv2.VideoWriter(
    "output/processed_video.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

detector = VehicleDetector()
counter = VehicleCounter(height // 2)

line_y = height // 2

total_detected = 0
count = 0

start_time = time.time()

while True:

    ret, frame = cap.read()

    if not ret:
        print("Video Finished")
        break

    detections = detector.detect(frame)

    total_detected += len(detections)

    count = counter.update(detections)

    cv2.line(
        frame,
        (0, line_y),
        (width, line_y),
        (0, 0, 255),
        2
    )

    for (x, y, w, h) in detections:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f"Vehicle Count: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.imshow("Traffic Monitoring", frame)

    output_video.write(frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

processing_time = time.time() - start_time

save_report(
    "traffic.mp4",
    total_detected,
    count,
    processing_time,
    "output/report.json"
)

cap.release()
output_video.release()
cv2.destroyAllWindows()

print("Processing Complete!")
print("Vehicle Count:", count)