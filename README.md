# Smart Traffic Monitoring and Vehicle Counting System

## Project Overview

The Smart Traffic Monitoring and Vehicle Counting System is a computer vision application developed using Python and OpenCV. The system processes a traffic video, detects moving vehicles, tracks them across video frames, counts vehicles crossing a predefined counting line, and generates traffic statistics.

This project demonstrates the practical application of image processing, object detection, object tracking, and traffic analytics using OpenCV.

---

## Objective

The objective of this project is to:

* Detect moving vehicles from a traffic video.
* Track vehicles across consecutive frames.
* Assign unique IDs to detected vehicles.
* Count vehicles only when they cross a predefined counting line.
* Count vehicles based on direction (Incoming and Outgoing).
* Generate useful traffic statistics.
* Save the processed video with annotations.
* Export results in JSON format.

---

## Technologies Used

* Python 3
* OpenCV
* NumPy
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

* Background subtraction using MOG2.
* Morphological operations for noise reduction.
* Contour detection for identifying moving vehicles.
* Bounding box generation around detected vehicles.

### Vehicle Tracking

* Centroid-based vehicle tracking.
* Unique vehicle ID assignment.
* Distance-based matching between consecutive frames.
* Vehicle center point visualization.

### Vehicle Counting

* Counting line drawn on the road.
* Vehicles counted only when crossing the line.
* Prevention of duplicate counting.
* Direction-based counting:

  * Incoming Vehicles
  * Outgoing Vehicles

### Real-Time Analytics

Displays:

* Total Vehicle Count
* Incoming Vehicle Count
* Outgoing Vehicle Count
* Total Detections
* Active Vehicles
* Frames Per Second (FPS)

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

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

requirements.txt

```text
opencv-python==4.13.0.92
numpy==2.3.0
```

---

## Running the Project

Navigate to the project directory and run:

```bash
python src/main.py
```

---

## Output

### Processed Video

The output video contains:

* Vehicle Bounding Boxes
* Vehicle IDs
* Vehicle Center Points
* Counting Line
* Incoming and Outgoing Counts
* Total Detections
* Active Vehicles
* FPS Display

### JSON Report

Example:

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

## Working Principle

1. Read the traffic video frame by frame.
2. Apply background subtraction to identify moving objects.
3. Perform image preprocessing and noise removal.
4. Detect contours corresponding to vehicles.
5. Draw bounding boxes around detected vehicles.
6. Calculate vehicle centroids.
7. Assign unique IDs to vehicles.
8. Track vehicles across frames using distance-based matching.
9. Count vehicles when they cross the counting line.
10. Determine vehicle direction (incoming or outgoing).
11. Display real-time traffic analytics.
12. Save processed video and generate JSON report.

---

## Improvements Implemented

The following enhancements were added:

* Unique Vehicle IDs
* Distance-Based Vehicle Tracking
* Direction-Based Counting
* Improved Contour Filtering
* Background Subtractor Optimization
* Vehicle Center Visualization
* FPS Monitoring
* Active Vehicle Monitoring
* Rich Traffic Analytics
* Enhanced JSON Reporting

---

## Future Enhancements

* Vehicle Classification (Car, Bus, Truck, Bike)
* Vehicle Speed Estimation
* Traffic Density Charts
* Streamlit Dashboard
* Deep Learning Based Detection (YOLO)
* Multi-Lane Traffic Analysis

---

## Conclusion

The Smart Traffic Monitoring and Vehicle Counting System successfully detects, tracks, and counts vehicles from traffic video footage. The system provides real-time traffic analytics and generates detailed reports, making it a practical demonstration of computer vision techniques applied to traffic monitoring.
