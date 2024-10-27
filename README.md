# Ingestion-Api-Analytics-Task
TASK 1 - DATA INGESTION &amp; PROCESSING
TASK 2 - BASIC REST API DEVELOPMENT
TASK 3 - SIMPLE DATA ANALYTICS

## Overview

**Ingestion-Api-Analytics-Task** is a Python-based project that involves three main tasks: data ingestion, REST API development, and data analytics. The project simulates machine data, processes it, and provides a REST API to interact with the data.

### Task 1: Data Ingestion & Processing

**Description:**  
A Python script reads a continuous stream of simulated machine data (temperature, speed, and status). The script:

- Reads data every 10 seconds from a JSON file or a mocked endpoint.
- Calculates a moving average for each parameter over the last 5 readings.
- Outputs the transformed data in JSON format.

**Evaluation Criteria:**
- Code clarity and simplicity.
- Correct implementation of moving average calculation.
- Efficient use of Python’s standard libraries.

### Task 2: Basic REST API Development

**Description:**  
A simple REST API using Flask that includes two endpoints:

- **GET** `/data`: Returns the processed machine data as JSON.
- **POST** `/status`: Allows updating the machine’s job status (e.g., “STARTED”, “COMPLETED”).

**Requirements:**
- Input validation for `/status` to allow only specific statuses.
- In-memory storage for machine status updates.

**Evaluation Criteria:**
- Ability to set up a basic Flask API.
- Proper input validation and error handling.
- Organized code structure.

### Task 3: Simple Data Analytics

**Description:**  
A Python function that reads a list of timestamps and values (e.g., machine speed) and calculates:

- The average value over the period.
- The maximum and minimum values.

**Bonus:**  
Detect anomalies where values deviate by more than 20% from the average.

**Evaluation Criteria:**
- Accurate calculations.
- Efficient, readable code.
- Bonus points for handling anomaly detection.

---

## Installation

To set up and run **Ingestion-Api-Analytics-Task**, follow these steps:

### Prerequisites

- Python 3.6 or higher
- `pip` package manager

### Steps to Install

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Ingestion-Api-Analytics-Task.git
   cd Ingestion-Api-Analytics-Task
