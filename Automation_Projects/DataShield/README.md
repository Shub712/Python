# 🛡️ Marvellous Data Shield System

> Automated Incremental Backup, ZIP Archiving, Logging & Email Notification System built using Python.

## 📌 Overview

Marvellous Data Shield System is a Python-based automation tool designed to perform periodic backups of a specified directory. The system intelligently copies only new or modified files using MD5 hash comparison, creates compressed ZIP archives, generates detailed logs, and sends backup reports via email.

This project demonstrates practical implementation of file system automation, backup management, data integrity verification, and email notification services.

---

## 🚀 Features

- Incremental Backup (copies only new or modified files)
- MD5 Hash-Based Change Detection
- Automatic Scheduled Backups
- ZIP Archive Creation
- Backup Activity Logging
- Email Notification with Attachments
- Backup Restoration Support
- Preserves Original Folder Structure

---

## 🏗️ Project Workflow

```text
Source Directory
       │
       ▼
MD5 Hash Comparison
       │
       ▼
Incremental Backup
       │
       ▼
Backup Folder
       │
       ▼
ZIP Archive Creation
       │
       ▼
Log Generation
       │
       ▼
Email Notification
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Core Development |
| Schedule | Task Scheduling |
| Hashlib | MD5 Hash Generation |
| Shutil | File Operations |
| Zipfile | ZIP Compression |
| SMTP | Email Notifications |
| OS Module | File Management |

---

## 📂 Project Structure

```text
Marvellous-Data-Shield/
│
├── DataShield.py
├── BackupFolder/
├── Report_YYYY-MM-DD.log
├── BackupFolder_YYYY-MM-DD.zip
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/marvellous-data-shield.git
cd marvellous-data-shield
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Linux / macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install schedule
```

---

## ▶️ Usage

### Start Automated Backup

```bash
python DataShield.py <TimeInterval> <SourceDirectory>
```

### Example

```bash
python DataShield.py 5 DataFolder
```

The above command will run the backup process every 5 minutes.

---

## 📦 Restore Backup

To restore a previously generated ZIP archive:

```bash
python DataShield.py --restore BackupFolder.zip RestoredFolder
```

### Example

```bash
python DataShield.py --restore BackupFolder_2026-06-04.zip RecoveryFolder
```

---

## 📋 Command Line Options

### Help

```bash
python DataShield.py --h
```

### Usage Guide

```bash
python DataShield.py --u
```

---

## 🔍 How It Works

1. Scans the source directory.
2. Generates MD5 hash for each file.
3. Compares hashes with files in the backup folder.
4. Copies only new or modified files.
5. Preserves directory structure.
6. Creates a ZIP archive of the backup.
7. Generates a log report.
8. Sends email notification with backup and log attachments.

---

## 📧 Email Configuration

Update the following credentials in the script:

```python
sender_email = "your_email@gmail.com"
app_password = "your_app_password"
receiver_mail = "receiver@gmail.com"
```

> Note: For Gmail, enable Two-Factor Authentication and generate an App Password.

---

## 📊 Sample Output

```text
--------------------------------------------------
Backup process started successfully
--------------------------------------------------

Files copied : 15

ZIP file created :
BackupFolder_2026-06-04_10-30-15.zip

--------------------------------------------------
Backup completed successfully
--------------------------------------------------
```

---

## 🔒 Security Considerations

- Avoid hardcoding email credentials.
- Store sensitive information using environment variables.
- Use secure SMTP connections (SSL/TLS).
- Consider replacing MD5 with SHA-256 for stronger integrity verification.

---

## 🚧 Future Enhancements

- GUI Dashboard (Tkinter / PyQt)
- Cloud Backup Integration (AWS S3, Google Drive)
- Backup Versioning
- Encrypted Backup Archives
- Multi-threaded Backup Engine
- Database Logging
- Docker Support
- Web-Based Monitoring Dashboard

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python Automation
- File Handling and Management
- Scheduling Tasks
- Data Integrity Verification
- ZIP Compression
- Email Automation
- System Utility Development

---

## 👨‍💻 Author

**Shubham Pawar**

Python Developer | Software Developer | Data Analyst | UI/UX Designer

GitHub: https://github.com/Shub712

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
