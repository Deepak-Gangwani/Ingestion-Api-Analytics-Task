# Ingestion-Api-Analytics-Task 🌐

![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.0.3-green) ![API](https://img.shields.io/badge/API-REST-orange) ![Data Processing](https://img.shields.io/badge/Data%20Processing-Ingestion-blueviolet)

![1_ebmDMPXU9xqgwqdob0XbKQ-ezgif com-crop](https://github.com/user-attachments/assets/b0ff241a-9e49-4a05-b4ad-26a294fb7125)
![RESTAPI](https://github.com/user-attachments/assets/78448e0b-d8ac-411b-98c5-2776d4b7f58e)
![images](https://github.com/user-attachments/assets/63adfb89-9fde-4077-a2c8-66427d343b0e)

![Machine-Data-Dashboard-ezgif com-crop](https://github.com/user-attachments/assets/42ea5018-5cfa-4241-9ecd-3406ffe4b4dc)
![Analytics-image](https://github.com/user-attachments/assets/a96ab195-5b11-47a8-a547-f9f939376679)
![outlier2](https://github.com/user-attachments/assets/040d077e-3939-4159-b9c9-59e1ef5e16df)

![fc71635c7f1b09ed30413f59bb749582](https://github.com/user-attachments/assets/3f9ca90e-187e-456a-8d66-d63b51aff854)





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
