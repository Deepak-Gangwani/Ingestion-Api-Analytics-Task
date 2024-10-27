import json
import time
from collections import deque
from statistics import mean
import requests  # Import requests for HTTP POST


class MachineDataSimulator:
    def __init__(self, api_url, status_url, window_size=5):
        # Initialize parameters
        self.api_url = api_url
        self.status_url = status_url
        self.window_size = window_size
        self.temperature_data = deque(maxlen=self.window_size)
        self.speed_data = deque(maxlen=self.window_size)
        self.machine_data = self._create_sample_data()

    def _create_sample_data(self):
        """Create sample machine data for simulation."""
        return [
            {"timestamp": "2024-10-27T12:00:00", "temperature": 70, "speed": 30, "status": "RUNNING"},
            {"timestamp": "2024-10-27T12:00:10", "temperature": 72, "speed": 32, "status": "RUNNING"},
            {"timestamp": "2024-10-27T12:00:20", "temperature": 75, "speed": 34, "status": "RUNNING"},
            {"timestamp": "2024-10-27T12:00:30", "temperature": 71, "speed": 29, "status": "RUNNING"},
            {"timestamp": "2024-10-27T12:00:40", "temperature": 74, "speed": 33, "status": "RUNNING"},
            {"timestamp": "2024-10-27T12:00:50", "temperature": 76, "speed": 35, "status": "RUNNING"},
            {"timestamp": "2024-10-27T12:01:00", "temperature": 78, "speed": 36, "status": "RUNNING"},
        ]

    def calculate_moving_average(self, data_stream):
        """Calculate moving average for temperature and speed."""
        self.temperature_data.append(data_stream["temperature"])
        self.speed_data.append(data_stream["speed"])

        return {
            "temperature_avg": mean(self.temperature_data) if self.temperature_data else None,
            "speed_avg": mean(self.speed_data) if self.speed_data else None,
            "timestamp": data_stream["timestamp"],
        }

    def send_to_api(self, data):
        """Send the processed moving average data to the Flask API."""
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            if response.status_code == 200:
                print("Data sent to API:", data)
            else:
                print("Failed to send data:", response.status_code, response.text)
        except requests.exceptions.RequestException as e:
            print("Error sending data to API:", e)

    def update_status(self, status):
        """Update the machine status in the Flask API."""
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(self.status_url, headers=headers, json={"status": status})
            if response.status_code == 200:
                print(f"Machine status updated to: {status}")
            else:
                print("Failed to update status:", response.status_code, response.text)
        except requests.exceptions.RequestException as e:
            print("Error updating status:", e)

    def run_simulation(self):
        """Run the simulation by sending moving averages to the API."""
        self.update_status("RUNNING")

        for data in self.machine_data:
            moving_avg_data = self.calculate_moving_average(data)
            print("Calculated Moving Average:", json.dumps(moving_avg_data, indent=2))
            self.send_to_api(moving_avg_data)
            time.sleep(10)  # Simulate delay in data processing

        self.update_status("COMPLETED")


if __name__ == "__main__":
    # URL of the Flask API
    API_URL = "http://127.0.0.1:5000/data"  # Localhost Flask server
    STATUS_URL = "http://127.0.0.1:5000/status"  # URL to update the status

    simulator = MachineDataSimulator(API_URL, STATUS_URL)
    simulator.run_simulation()
