# Smart Traffic Monitoring and Vehicle Counting System using YOLOv8 and OpenCV

## Project Overview

The Smart Traffic Monitoring and Vehicle Counting System is a computer vision application developed using Python, OpenCV, and YOLOv8. The system processes traffic videos, detects vehicles, tracks their movement across frames, counts vehicles crossing a predefined line, and generates detailed traffic analytics.

Unlike traditional contour-based methods, this project uses YOLOv8 object detection to accurately identify vehicles such as cars, buses, trucks, and motorcycles, resulting in improved detection accuracy and reduced false positives.

---

## Objective

The objective of this project is to:

* Detect vehicles from traffic video footage.
* Track vehicles across multiple frames.
* Assign unique IDs to detected vehicles.
* Count vehicles crossing a counting line.
* Count vehicles based on travel direction.
* Generate traffic statistics and analytics.
* Save processed video with annotations.
* Export traffic reports in JSON format.

---

## Technologies Used

* Python 3
* OpenCV
* NumPy
* YOLOv8 (Ultralytics)
* JSON

---

## Project Structure

```text
vehicle_count/

├── input/
│   └── traffic.mp4

├── output/
│   ├── processed_video.mp4
│   └── report.json

├── src/
│   ├── detector.py
│   ├── counter.py
│   ├── utils.py
│   └── main.py

├── requirements.txt
└── README.md
```

---

## Features

### Vehicle Detection

* YOLOv8 object detection model.
* Detects:

  * Cars
  * Motorcycles
  * Buses
  * Trucks
* Generates accurate bounding boxes.
* Reduces false detections caused by shadows and road markings.

### Vehicle Tracking

* Centroid-based tracking.
* Unique vehicle ID assignment.
* Distance-based object matching.
* Vehicle center point visualization.

### Vehicle Counting

* Counts vehicles only when they cross the counting line.
* Prevents duplicate counting.
* Supports incoming and outgoing vehicle counting.
* Uses tracked vehicle IDs for accurate counting.

### Real-Time Analytics

Displays:

* Total Vehicle Count
* Incoming Vehicle Count
* Outgoing Vehicle Count
* Active Vehicle Count
* Total Detections
* FPS (Frames Per Second)

### Reporting

Generates a JSON report containing:

* Video Name
* Total Vehicles Detected
* Total Vehicles Counted
* Incoming Vehicles
* Outgoing Vehicles
* Vehicles Per Minute
* Processing Time

---

## Installation

### Step 1: Create Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

Create a file named `requirements.txt` with:

```text
opencv-python
numpy
ultralytics
```

---

## Running the Project

Navigate to the project directory and execute:

```bash
python src/main.py
```

---

## Working Principle

1. Read traffic video frame by frame.
2. Use YOLOv8 to detect vehicles.
3. Generate bounding boxes around detected vehicles.
4. Calculate vehicle center points.
5. Assign unique IDs using centroid tracking.
6. Track vehicles across consecutive frames.
7. Detect line crossing events.
8. Determine vehicle direction (Incoming or Outgoing).
9. Display real-time analytics.
10. Save processed video.
11. Generate JSON traffic report.

---

## Output

### Processed Video

The processed video contains:

* Vehicle Bounding Boxes
* Vehicle IDs
* Vehicle Center Points
* Counting Line
* Total Vehicle Count
* Incoming Count
* Outgoing Count
* Active Vehicle Count
* Total Detections
* FPS Display

### Sample JSON Report

```json
{
    "video_name": "traffic.mp4",
    "total_vehicles_detected": 245,
    "total_vehicles_counted": 198,
    "incoming_vehicles": 104,
    "outgoing_vehicles": 94,
    "vehicles_per_minute": 62.4,
    "processing_time_seconds": 32.5
}
```

---

## Improvements Implemented

The following improvements were added compared to the basic OpenCV implementation:

* YOLOv8 Vehicle Detection
* Vehicle Classification (Car, Bus, Truck, Motorcycle)
* Centroid-Based Vehicle Tracking
* Unique Vehicle IDs
* Distance-Based Matching
* Direction-Based Counting
* Improved Counting Accuracy
* Vehicle Center Visualization
* FPS Monitoring
* Active Vehicle Monitoring
* Enhanced Traffic Analytics
* JSON Report Generation

---

## Advantages

* Higher detection accuracy than contour-based methods.
* Reduced false detections from shadows and noise.
* Better handling of closely spaced vehicles.
* Supports multiple vehicle types.
* Generates detailed traffic analytics.
* Scalable for real-world traffic monitoring applications.

---

## Future Enhancements

* Vehicle Speed Estimation
* DeepSORT Tracking Integration
* Multi-Lane Vehicle Analysis
* Traffic Density Graphs
* Streamlit Dashboard
* Real-Time CCTV Monitoring
* Vehicle Type Statistics
* Cloud-Based Analytics

---

## Conclusion

The Smart Traffic Monitoring and Vehicle Counting System successfully combines YOLOv8 object detection with OpenCV-based tracking and analytics to provide an accurate and efficient traffic monitoring solution. The system detects, tracks, and counts vehicles while generating detailed traffic statistics and reports, demonstrating the practical application of computer vision in intelligent transportation systems.
