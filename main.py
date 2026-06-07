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

output_video = cv2.VideoWriter(
    "output/processed_video.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

detector = VehicleDetector()

line_y = int(height * 0.7)

counter = VehicleCounter(line_y)

total_detected = 0

start_time = time.time()

while True:

    frame_start = time.time()

    ret, frame = cap.read()

    if not ret:
        break

    detections = detector.detect(frame)

    total_detected += len(detections)

    total_count, incoming_count, outgoing_count, tracked_vehicles = counter.update(
        detections
    )

    active_vehicles = len(tracked_vehicles)

    cv2.line(
        frame,
        (0, line_y),
        (width, line_y),
        (0, 0, 255),
        3
    )

    for (x, y, w, h) in detections:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cx = x + w // 2
        cy = y + h // 2

        cv2.circle(
            frame,
            (cx, cy),
            4,
            (0, 0, 255),
            -1
        )

        for vehicle_id, data in tracked_vehicles.items():

            tx, ty = data["center"]

            if abs(tx - cx) < 30 and abs(ty - cy) < 30:

                cv2.putText(
                    frame,
                    f"ID:{vehicle_id}",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 0),
                    2
                )

                break

    current_fps = 1 / (time.time() - frame_start)

    cv2.putText(
        frame,
        f"Total Count: {total_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        f"Incoming: {incoming_count}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Outgoing: {outgoing_count}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Detections: {total_detected}",
        (20, 160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"FPS: {current_fps:.2f}",
        (20, 200),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Active Vehicles: {active_vehicles}",
        (20, 240),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imshow(
        "Smart Traffic Monitoring System",
        frame
    )

    output_video.write(frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

processing_time = time.time() - start_time

save_report(
    "traffic.mp4",
    total_detected,
    total_count,
    incoming_count,
    outgoing_count,
    processing_time,
    "output/report.json"
)

cap.release()
output_video.release()
cv2.destroyAllWindows()

print("Processing Complete")
print("Total Vehicles:", total_count)
print("Incoming Vehicles:", incoming_count)
print("Outgoing Vehicles:", outgoing_count)
