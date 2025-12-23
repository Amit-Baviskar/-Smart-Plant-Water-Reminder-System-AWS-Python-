# -Smart-Plant-Water-Reminder-System-AWS-Python-

---

## 📌 Table of Contents

1. [Overview](#overview)  
2. [Architecture](#architecture)  
3. [Features](#features)  
4. [Tech Stack](#tech-stack)   
5. [Project Flow](#project-flow)  
6. [Getting Started](#getting-started)  
7. [Key Takeaways](#key-takeaways)  
8. [Future Enhancements](#future-enhancements)  
---

## 🌟 Overview

This project simulates a smart garden system that:
- Sends real-time soil moisture data using a Python script
- Streams the data to AWS using **Kinesis Data Streams**
- Triggers an **AWS Lambda function** when data is received
- Sends **email alerts** via **Amazon SNS** based on critical thresholds

---

##  Architecture





![Image](https://github.com/user-attachments/assets/8396ade3-df19-41e1-97ad-d270b7984f60)


---

##  Features

- 🔁 Continuous simulation of soil sensor readings (value from 100 to 0)
- 📡 Real-time data ingestion via Kinesis
- 🧠 Intelligent threshold-based alerts:
  - 85 → "Water the plant"
  - 0  → "Plant is dying"
- 📬 Instant email notifications using Amazon SNS
- ☁️ Fully serverless and scalable architecture

---

##  Tech Stack

- **Python** – for data simulation and scripting
- **AWS Kinesis Data Streams** – to stream real-time data
- **AWS Lambda** – serverless compute to process sensor data
- **Amazon SNS** – email notifications
- **IAM Roles** – for access and permissions
- *(Optional)*: CloudWatch, Terraform, S3 for logging or extensions

---

##  Project Flow

1. Python script generates fake sensor values (100 → 0)
2. Each value is sent to a **Kinesis Data Stream**
3. **Lambda function** is triggered on incoming stream data
4. If sensor value:
   - == 85 → Email: "Time to water the plant"
   - == 0 → Email: "Critical! The plant is dying."
5. Emails are sent through **Amazon SNS**

--- 

## 2. Setup SNS Topic
 
 * Create a topic in SNS

 * Subscribe your email

 * Confirm the subscription from your inbox


---

## 3. Create Kinesis Stream

    aws kinesis create-stream --stream-name plant-sensor-stream --shard-count 1


## 4. Deploy Lambda & Connect to Kinesis

Use the provided Lambda code from lambda_function.py

Create the event source mapping:


    aws lambda create-event-source-mapping \
    --function-name PlantWaterCheck \
    --event-source-arn arn:aws:kinesis:your-region:your-account-id:stream/plant-sensor-stream \
    --starting-position LATEST


  ---
  
## 5. Run the Python Sensor Script


     python simulate_sensor.py


--- 

 Key Takeaways

 * Gained real-world experience with AWS event-driven architecture

 * Practiced threshold-based email alerting using Lambda + SNS

 * Learned how to stream data in real time using Kinesis

 * Applied DevOps principles to automate and monitor workflows

---

 Future Enhancements

* ✅ Replace simulated data with actual soil sensor (e.g., DHT11/DHT22 + Raspberry Pi)

* ✅ Add S3 or DynamoDB for historical sensor data logging

* ✅ Integrate with mobile notifications (SMS, push)

* ✅ Build a real-time dashboard (QuickSight / Streamlit)

* ✅ Use AWS IoT Core for better IoT scalability


 License
This project is open-source and available under the MIT License.

