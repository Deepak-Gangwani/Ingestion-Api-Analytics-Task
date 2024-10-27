# Ingestion-Api-Analytics-Task 🌐

![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.0.3-green) ![API](https://img.shields.io/badge/API-REST-orange) ![Data Processing](https://img.shields.io/badge/Data%20Processing-Ingestion-blueviolet)

![Machine-Data-Dashboard-ezgif com-crop](https://github.com/user-attachments/assets/42ea5018-5cfa-4241-9ecd-3406ffe4b4dc)
![Analytics-image](https://github.com/user-attachments/assets/a96ab195-5b11-47a8-a547-f9f939376679)


<div align="center">
    <img src="https://user-images.githubusercontent.com/your_username/machine-data-gif.gif" width="600" alt="Machine Data Monitoring in Action" />
    <p>Machine Data Monitoring - Ingestion & Analytics Workflow</p>
</div>

---

## 📖 Project Overview

**Ingestion-Api-Analytics-Task** is a comprehensive Python project that simulates machine data ingestion, processing, and analysis. It reads data streams, computes moving averages, provides an API to interact with the data, and includes statistical analysis with anomaly detection.

### 🔑 Key Features

- **Simulated Data Ingestion**: Reads machine data every 10 seconds.
- **REST API Endpoints**: Fetch processed data and update machine status.
- **Data Analytics**: Provides insights like average, max, min, and anomaly detection.

---

## 🛠️ Project Structure

```plaintext
Ingestion-Api-Analytics-Task/
├── app.py                # Flask API server
├── ingestion.py          # Data ingestion and processing
├── analytics.py          # Data analytics functions
├── README.md             # Project documentation
├── requirements.txt      # Dependencies
└── templates/            # Folder for HTML templates
    └── index.html        # Main HTML template file
```

## 📝 Project Implementation

### 🧩 Task 1: Data Ingestion & Processing
In ingestion.py, this script reads machine data every 10 seconds from a mocked endpoint or JSON file, computes a moving average over the last 5 readings, and displays the results in JSON format.
