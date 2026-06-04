import json

def save_report(
        video_name,
        total_detected,
        total_counted,
        processing_time,
        output_path):

    report = {
        "video_name": video_name,
        "total_vehicles_detected": total_detected,
        "total_vehicles_counted": total_counted,
        "processing_time_seconds": round(processing_time, 2)
    }

    with open(output_path, "w") as file:
        json.dump(report, file, indent=4)