# 📂 Directory Organiser

An automated Python utility that organises files into folders based on their file extensions. The script continuously monitors a directory and automatically moves files into categorized folders while generating detailed log reports.

---

## 🚀 Features

- Automatically sorts files based on file extensions.
- Creates extension-specific folders dynamically.
- Handles files without extensions using a dedicated `NoExtension` folder.
- Generates execution logs with statistics.
- Runs continuously using a scheduler.
- Lightweight and easy to configure.
- Cross-platform support (Windows, Linux, macOS).

---

## 📁 Project Structure

```text
DirectoryOrganiser/
│
├── DirectoryOrganiser.py
├── README.md
│
├── txt/
├── jpg/
├── pdf/
├── csv/
└── NoExtension/
```

---

## ⚙️ How It Works

Suppose a directory contains:

```text
Demo/
│
├── Notes.txt
├── Image.jpg
├── Data.csv
└── README
```

After execution:

```text
Demo/
│
├── txt/
│   └── Notes.txt
│
├── jpg/
│   └── Image.jpg
│
├── csv/
│   └── Data.csv
│
└── NoExtension/
    └── README
```

---

## 🛠️ Technologies Used

- Python 3.x
- os
- shutil
- schedule
- sys
- time

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/DirectoryOrganiser.git

cd DirectoryOrganiser
```

### Install Dependencies

```bash
pip install schedule
```

---

## ▶️ Usage

### Run Program

```bash
python DirectoryOrganiser.py <DirectoryPath>
```

### Example

```bash
python DirectoryOrganiser.py Demo
```

The application will:

1. Monitor the directory.
2. Check every minute.
3. Organise newly added files automatically.
4. Generate log files after each successful operation.

---

## 📋 Command Line Options

### Help

```bash
python DirectoryOrganiser.py --h
```

Output:

```text
This script sorts files based on their extensions.
It creates a new folder for each extension.
```

### Usage

```bash
python DirectoryOrganiser.py --u
```

Output:

```text
Usage:
python DirectoryOrganiser.py SourceDirectory
```

---

## 📝 Sample Log File

```text
-------------------------------------------------
----- Log File Created By Automation Script -----
Directories Made        : 5
Files With No Extension : 2
Files Moved             : 18
-------------------------------------------------
```

Log files are generated with timestamped names:

```text
Report_20260210_183015.log
```

---

## 🔄 Scheduler

The application uses the Schedule library and executes the organisation task every minute.

```python
schedule.every(1).minutes.do(job, directory)
```

This allows automatic sorting of newly added files without restarting the program.

---

## 📊 Statistics Tracked

| Metric | Description |
|----------|------------|
| Directories Made | Number of folders created |
| Files Moved | Number of files organised |
| Files Without Extension | Files moved to NoExtension folder |

---

## 🔒 Error Handling

The application validates:

- Directory existence
- Valid directory path
- Missing command-line arguments
- Help and usage requests

---

## 💡 Future Enhancements

- GUI version using Tkinter or PyQt.
- Real-time monitoring using Watchdog.
- Duplicate file detection.
- File size-based sorting.
- Date-wise organisation.
- Extension mapping (Images, Documents, Videos).
- Email notifications.
- Database logging.

---

## 👨‍💻 Author

**Shubham Kiran Pawar**

- Python Developer
- Data Science & AI Enthusiast

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful:

- Star the repository
- Fork the project
- Create pull requests
- Share feedback

Happy Coding! 🚀
