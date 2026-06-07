import json

def save_report(
        video_name,
        total_detected,
        total_counted,
        incoming_count,
        outgoing_count,
        processing_time,
        output_path):

    vehicles_per_minute = 0

    if processing_time > 0:

        vehicles_per_minute = (
            total_counted /
            processing_time
        ) * 60

    report = {

        "video_name": video_name,

        "total_vehicles_detected":
            total_detected,

        "total_vehicles_counted":
            total_counted,

        "incoming_vehicles":
            incoming_count,

        "outgoing_vehicles":
            outgoing_count,

        "vehicles_per_minute":
            round(vehicles_per_minute, 2),

        "processing_time_seconds":
            round(processing_time, 2)
    }

    with open(output_path, "w") as file:
        json.dump(report, file, indent=4)
