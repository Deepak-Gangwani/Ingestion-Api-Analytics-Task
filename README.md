# Ingestion-Api-Analytics-Task 🌐

![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.0.3-green) ![API](https://img.shields.io/badge/API-REST-orange) ![Data Processing](https://img.shields.io/badge/Data%20Processing-Ingestion-blueviolet)

## 📖 Project Overview

**Ingestion-Api-Analytics-Task** is a comprehensive Python project that simulates machine data ingestion, processing, and analysis. It reads data streams, computes moving averages, provides an API to interact with the data, and includes statistical analysis with anomaly detection.

![fc71635c7f1b09ed30413f59bb749582](https://github.com/user-attachments/assets/3f9ca90e-187e-456a-8d66-d63b51aff854)

### 🔑 Key Features

- **Simulated Data Ingestion**: Reads machine data every 10 seconds.
- **REST API Endpoints**: Fetch processed data and update machine status.
- **Data Analytics**: Provides insights like average, max, min, and anomaly detection.

---

<div align="center">
    <img src="https://user-images.githubusercontent.com/your_username/machine-data-gif.gif" width="600" alt="Machine Data Monitoring in Action" />
    <p>Machine Data Monitoring - Ingestion & Analytics Workflow</p>
</div>

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

### 🛠️ Task 1: Data Ingestion & Processing

#### Description:
In this task, a Python script is developed to simulate the continuous stream of machine data (including parameters such as temperature, speed, and status). The script is designed to read this data every 10 seconds from a specified JSON file or a mocked endpoint.

###### Key Features:
- Data Reading: The script reads machine data at regular intervals (every 10 seconds).
- Data Transformation: It calculates a moving average for each parameter over the last five readings, providing insights into the machine's performance.
- Output Format: The transformed data is printed in JSON format for easy readability and further processing.
  
#####Evaluation Criteria:
- Code clarity and simplicity to ensure maintainability.
- Correct implementation of moving average calculation to ensure accuracy.
- Efficient use of Python’s standard libraries to optimize performance.

![Machine-Data-Dashboard-ezgif com-crop](https://github.com/user-attachments/assets/42ea5018-5cfa-4241-9ecd-3406ffe4b4dc)

### 🌐 Task 2: Basic REST API Development
####Description:
This task involves building a simple REST API using Flask that exposes two key endpoints.

##### Endpoints:
- [GET] /data: Returns the processed machine data as JSON, allowing clients to retrieve the latest calculated metrics.
- [POST] /status: Enables updating the machine's job status (e.g., “STARTED”, “COMPLETED”). This helps keep track of the machine's operational state.
  
##### Requirements:
- Input validation for the /status endpoint to ensure only acceptable statuses are processed.
- Management of machine status updates in memory for quick access and manipulation.
  
##### Evaluation Criteria:
- Ability to set up a basic Flask API structure.
- Proper input validation and error handling to enhance robustness.
- Well-organized code to improve readability and maintainability.

### 📈 Task 3: Simple Data Analytics

#### Description:
In this final task, a Python function is implemented to perform data analytics on the machine data. The function reads a list of timestamps and values (e.g., machine speed) and calculates various statistics.

##### Calculations:
- Average Value: Computes the average of the collected data over the entire period.
- Maximum and Minimum Values: Identifies the peak and lowest readings for performance monitoring.
  
##### Bonus Feature:
If time permits, the candidate can extend the function to detect anomalies—specifically, any values that deviate by more than 20% from the calculated average. This enhances the functionality by providing early warning indicators for potential issues.

##### Evaluation Criteria:
- Accuracy of calculations to ensure reliable data analytics.
- Code efficiency and readability to facilitate future modifications.
- Bonus points awarded for implementing anomaly detection, adding extra value to the solution.
  
![RESTAPI](https://github.com/user-attachments/assets/78448e0b-d8ac-411b-98c5-2776d4b7f58e)
![outlier2](https://github.com/user-attachments/assets/040d077e-3939-4159-b9c9-59e1ef5e16df)
![Analytics-image](https://github.com/user-attachments/assets/a96ab195-5b11-47a8-a547-f9f939376679)

## Contributing 🤝
We welcome contributions from the community! Your input helps make this project better for everyone. To contribute, please follow these steps:
- Create a Pull Request: Go to the original repository and click the “New Pull Request” button. 
- Provide a detailed description of your changes and submit your pull request.

Thank you for considering contributing to this project! Your efforts are greatly appreciated! 🌟

## License 📄
This project is licensed under the MIT License. This means you are free to use, modify, and distribute the project as long as you include the original license and copyright notice.

## Support 🙋‍♂️
If you have any questions, issues, or suggestions regarding this project, feel free to reach out!

- Open an Issue: If you encounter bugs or have feature requests, please open an issue in the GitHub repository.
- Discussion Forum: Join our Discussion Forum to engage with the community and share ideas.
- Contact Us: You can also reach me directly at deepakgangwani512@gmail.com for any specific inquiries.
  
#### Your feedback is valuable and helps us improve! Thank you for your support! ❤️


![images](https://github.com/user-attachments/assets/63adfb89-9fde-4077-a2c8-66427d343b0e)


![Machine-Data-Dashboard-ezgif com-crop](https://github.com/user-attachments/assets/42ea5018-5cfa-4241-9ecd-3406ffe4b4dc)
![Analytics-image](https://github.com/user-attachments/assets/a96ab195-5b11-47a8-a547-f9f939376679)


![1_ebmDMPXU9xqgwqdob0XbKQ-ezgif com-crop](https://github.com/user-attachments/assets/b0ff241a-9e49-4a05-b4ad-26a294fb7125)
![RESTAPI](https://github.com/user-attachments/assets/78448e0b-d8ac-411b-98c5-2776d4b7f58e)
![outlier2](https://github.com/user-attachments/assets/040d077e-3939-4159-b9c9-59e1ef5e16df)
