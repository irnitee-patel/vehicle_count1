import math

class VehicleCounter:

    def __init__(self, line_y):

        self.line_y = line_y
        self.next_id = 1
        self.vehicles = {}

        self.total_count = 0
        self.incoming_count = 0
        self.outgoing_count = 0

    def update(self, detections):

        current_centers = []

        for (x, y, w, h) in detections:

            cx = x + w // 2
            cy = y + h // 2

            current_centers.append((cx, cy))

        for center in current_centers:

            cx, cy = center

            matched_id = None

            for vehicle_id, data in self.vehicles.items():

                old_x, old_y = data["center"]

                distance = math.sqrt(
                    (cx - old_x) ** 2 +
                    (cy - old_y) ** 2
                )

                if distance < 100:
                    matched_id = vehicle_id
                    break

            if matched_id is None:

                self.vehicles[self.next_id] = {
                    "center": (cx, cy),
                    "counted": False
                }

                self.next_id += 1

            else:

                old_y = self.vehicles[matched_id]["center"][1]

                if (
                    old_y < self.line_y
                    and cy >= self.line_y
                    and not self.vehicles[matched_id]["counted"]
                ):

                    self.total_count += 1
                    self.outgoing_count += 1

                    self.vehicles[matched_id]["counted"] = True

                elif (
                    old_y > self.line_y
                    and cy <= self.line_y
                    and not self.vehicles[matched_id]["counted"]
                ):

                    self.total_count += 1
                    self.incoming_count += 1

                    self.vehicles[matched_id]["counted"] = True

                self.vehicles[matched_id]["center"] = (cx, cy)

        return (
            self.total_count,
            self.incoming_count,
            self.outgoing_count,
            self.vehicles
        )
