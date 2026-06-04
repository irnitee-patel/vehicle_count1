# vehicle_count1
# Smart Traffic Monitoring and Vehicle Counting System

## Project Overview

This project is a Computer Vision application developed using Python and OpenCV. The system processes a traffic video, detects moving vehicles, tracks their movement, counts vehicles crossing a predefined line, and generates traffic statistics in JSON format.

## Objective

The objective of this project is to implement vehicle detection and counting using OpenCV techniques such as:

* Video Processing
* Background Subtraction
* Image Preprocessing
* Contour Detection
* Object Tracking
* Vehicle Counting
* JSON Report Generation

## Technologies Used

* Python 3
* OpenCV
* NumPy
* JSON

## Project Structure

project/

├── input/

│ └── traffic.mp4

├── output/

│ ├── processed_video.mp4

│ └── report.json

├── src/

│ ├── detector.py

│ ├── counter.py

│ ├── utils.py

│ └── main.py

├── requirements.txt

└── README.md

## Features

* Reads traffic video frame by frame.
* Detects moving vehicles using Background Subtraction.
* Draws bounding boxes around detected vehicles.
* Creates a counting line on the road.
* Counts vehicles crossing the line.
* Displays live vehicle count.
* Saves processed output video.
* Generates traffic statistics report in JSON format.

## Installation

Install the required libraries:

pip install -r requirements.txt

## Running the Project

Navigate to the project folder and execute:

python src/main.py

## Output

The application generates:

1. Processed Video

   * Vehicle Bounding Boxes
   * Counting Line
   * Live Vehicle Count

2. JSON Report

Example:

{
"video_name": "traffic.mp4",
"total_vehicles_detected": 245,
"total_vehicles_counted": 198,
"processing_time_seconds": 32.5
}

## Working Principle

1. Load the traffic video.
2. Apply background subtraction to identify moving objects.
3. Perform thresholding and morphological operations to remove noise.
4. Detect contours of moving vehicles.
5. Draw bounding boxes around detected vehicles.
6. Track vehicle centers.
7. Count vehicles crossing the predefined counting line.
8. Save processed video and statistics report.

## Future Enhancements

* Vehicle classification (car, bus, truck, bike)
* Speed estimation
* Direction-based vehicle counting
* Streamlit dashboard integration
* Traffic density analysis graphs

## Author

Irnitee C. Patel

## Conclusion

The Smart Traffic Monitoring and Vehicle Counting System demonstrates the practical application of OpenCV in traffic surveillance. The project successfully detects and counts vehicles from video footage while generating useful traffic statistics for analysis.
