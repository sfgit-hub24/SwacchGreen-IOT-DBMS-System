# SwacchGreen-IOT-DBMS-System
---
# 🌱 SwacchGreen

## Smart Waste Management System using Flask, MySQL, and IoT

SwacchGreen is an intelligent waste management platform designed to promote cleaner communities through citizen participation, real-time waste reporting, and IoT-enabled smart bin monitoring.

The system allows users to report waste issues, monitor smart bins, earn rewards for environmental contributions, and enables administrators to efficiently manage complaints and waste collection operations.

---

##  Features

###  User Features

* User Registration
* User Login
* Waste Issue Reporting
* Dashboard Overview
* Smart Bin Monitoring
* Reward Tracking

###  Admin Features

* Admin Dashboard
* Complaint Management
* User Monitoring
* Smart Bin Status Monitoring
* Waste Collection Tracking

###  IoT Features

* Real-time Bin Fill Level Monitoring
* Overflow Detection
* Collection Alerts
* Smart Waste Analytics

---

##  Technology Stack

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Backend

* Python
* Flask

### Database

* MySQL

### IoT Hardware

* ESP32 / Arduino
* Ultrasonic Sensor
* WiFi Module

### Tools

* VS Code
* Git
* GitHub

---

##  Project Structure

```text
SwacchGreen/
│
├── app.py
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── report.html
│   ├── bins.html
│   └── admin.html
│
└── README.md
```

---

##  Database Tables

### Users
  _ _ _ _ _ _ _ _ _ _
| Field    | Type    |
| -------- | ------- |
| UserID   | INT     |
| Name     | VARCHAR |
| Email    | VARCHAR |
| Password | VARCHAR |
  _ _ _ _ _ _ _ _ _ _

### Complaints
 _ _ _ _ _ _ _ _ _ _ _ _
| Field       | Type    |
| ----------- | ------- |
| ComplaintID | INT     |
| Location    | VARCHAR |
| Description | TEXT    |
| Status      | VARCHAR |
 _ _ _ _ _ _ _ _ _ _ _ _

### SmartBins
  _ _ _ _ _ _ _ _ _ _ 
| Field     | Type    |
| --------- | ------- |
| BinID     | INT     |
| BinName   | VARCHAR |
| FillLevel | INT     |
| Status    | VARCHAR |
 _ _ _ _ _ _ _ _ _ _ _

### Rewards
 _ _ _ _ _ _ _ _ _ 
| Field    | Type |
| -------- | ---- |
| RewardID | INT  |
| UserID   | INT  |
| Points   | INT  |
 _ _ _ _ _ _ _ _ _ 

---

##  Installation

### Clone Repository

```bash
git clone https://github.com/sfgithub-24/SwacchGreen-IOT-DBMS-System.git
```

### Move into Project Directory

```bash
cd SwacchGreen-IOT-DBMS-System
```

### Install Dependencies

```bash
pip install flask
pip install mysql-connector-python
```

### Run Application

```bash
python app.py
```

### Application URL

```text
http://127.0.0.1:5000
```


---

##  System Modules

### Home Page

Modern landing page introducing SwacchGreen.

### Dashboard

Displays:

* Users
* Complaints
* Rewards
* Smart Bins

### Report Module

Allows citizens to submit waste complaints.

### Smart Bin Monitoring

Displays IoT bin fill levels.

### Admin Dashboard

Provides complaint management and system overview.

---

## 🔮 Future Enhancements

* AI-based Waste Classification
* Image Upload for Complaints
* GPS-based Complaint Mapping
* Real-Time IoT Integration
* Mobile Application
* Route Optimization for Waste Collection Vehicles

---

## 👩‍💻 Developed By

**Safa Fatima**
**Sumaiyah Sajid**

B.Tech Computer Science Engineering


---

##  License

This project is developed for educational, research, and smart city innovation purposes.
