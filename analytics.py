import json

def analyze_data(timestamps, values):
    """
    Analyze machine speed data to calculate average, max, min values, and detect anomalies.

    Parameters:
        timestamps (list): List of timestamp strings.
        values (list): List of numerical values representing machine speed.

    Returns:
        dict: A dictionary containing average, max, min values, list of anomalies, and timestamps.
    """
    if not values:
        return {
            "timestamps": timestamps,
            "average": None,
            "max": None,
            "min": None,
            "anomalies": []
        }

    average_value = sum(values) / len(values)
    max_value = max(values)
    min_value = min(values)

    # Detect anomalies (values deviating more than 20% from the average)
    anomalies = [
        val for val in values if abs(val - average_value) > 0.2 * average_value
    ]

    return {
        "average": average_value,
        "max": max_value,
        "min": min_value,
        "anomalies": anomalies
    }


# Sample data
timestamps = [
    "2024-10-27T12:00:00", 
    "2024-10-27T12:00:10", 
    "2024-10-27T12:00:20",
    "2024-10-27T12:00:30",  # New timestamp
    "2024-10-27T12:00:40"   # New timestamp
]
values = [30, 32, 50, 31, 29]  # Two new values

# Analyze data and print results
result = analyze_data(timestamps, values)
print(json.dumps(result, indent=2))
