# 🖥️ Platform Surveillance System

## 📌 Overview

Platform Surveillance System is a Python-based automation tool that continuously monitors system resources and generates detailed log reports at user-defined intervals.

The application collects information about:

- CPU Usage
- RAM Usage
- Disk Usage
- Network Statistics
- Running Processes
- Process CPU Consumption
- Process Memory Consumption
- Thread Information

Generated reports are automatically stored as timestamped log files inside a specified directory.

---

## 🚀 Features

✅ Automatic Log Generation

✅ Periodic Monitoring using Scheduler

✅ CPU Usage Monitoring

✅ RAM Usage Monitoring

✅ Disk Usage Monitoring

✅ Network Traffic Monitoring

✅ Running Process Information

✅ Process Thread Count

✅ Timestamped Log Files

✅ Linux & Windows Compatible

---

## 🛠️ Technologies Used

- Python 3
- psutil
- schedule
- os
- sys
- time

---

## 📂 Project Structure

```text
Platform_Surveillance_System/
│
├── Surveillance.py
├── Logs/
│   ├── Marvellous_2026-02-10_12-00-00.log
│   └── Marvellous_2026-02-10_12-05-00.log
│
└── README.md
```

---

## 📥 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Platform_Surveillance_System.git

cd Platform_Surveillance_System
```

### Install Dependencies

```bash
pip install psutil schedule
```

---

## ▶️ Usage

### Help Menu

```bash
python3 Surveillance.py --h
```

### Usage Information

```bash
python3 Surveillance.py --u
```

### Start Monitoring

```bash
python3 Surveillance.py 5 Logs
```

Where:

- `5` = Time interval in minutes
- `Logs` = Directory where log files will be stored

Example:

```bash
python3 Surveillance.py 10 SystemLogs
```

This command creates a new log file every 10 minutes inside the `SystemLogs` directory.

---

## 📄 Sample Log Information

The generated log file contains:

```text
CPU Usage : 12.5 %

RAM Usage : 45.7 %

Disk Usage Report

/ -> 65 % Used

Network Usage Report

Sent : 150.25 MB
Received : 820.45 MB

PID : 1234
Name : chrome
Thread Count : 45
UserName : shubham
Status : running
CPU % : 2.5
Memory % : 3.8
```

---

## ⚙️ Process Information Captured

For every running process:

- Process ID (PID)
- Process Name
- Username
- Process Status
- Creation Time
- CPU Utilization
- Memory Utilization
- Thread Count

---

## 📊 System Information Captured

### CPU

- Total CPU Usage Percentage

### Memory

- RAM Usage Percentage

### Storage

- Usage Percentage of Mounted Partitions

### Network

- Bytes Sent
- Bytes Received

---

## 📝 Example Output

```bash
----------------------------------------------------
------ Marvellous Platform Surveillance System -----
----------------------------------------------------

Platform Surveillance System Started Successfully

Directory Created With Name : Logs

Time Interval in Minutes : 5

Press Ctrl + C to stop execution
```

---

## 🔮 Future Enhancements

- Email Log Reports
- CSV Report Generation
- PDF Report Generation
- Threshold-Based Alerts
- Process Filtering
- Real-Time Dashboard
- Database Integration

---

## 👨‍💻 Author

**Shubham Kiran Pawar**

Python Developer | Data Science Enthusiast

---

## 📜 License

This project is developed for educational and learning purposes.
