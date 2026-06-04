# 🗂️ Disk Sanitizer

> A Python automation tool that detects and removes duplicate files from a directory using MD5 hash comparison.

---

## 📌 Overview

Duplicate File Remover is a Python-based utility that scans a specified directory and its subdirectories to identify files with identical content. The application generates MD5 checksums for every file and compares them to detect duplicates.

Once duplicate files are identified, the script automatically removes redundant copies while keeping a single original file, helping users free up disk space and maintain organized storage.

---

## 🚀 Features

- Recursive Directory Scanning
- MD5 Hash-Based File Comparison
- Duplicate File Detection
- Automatic Duplicate File Removal
- Preserves One Original Copy
- Displays Deleted Files Information
- Storage Space Optimization

---

## 🏗️ Project Workflow

```text
User Directory
       │
       ▼
Scan All Files
       │
       ▼
Generate MD5 Hash
       │
       ▼
Compare Checksums
       │
       ▼
Identify Duplicates
       │
       ▼
Delete Redundant Files
       │
       ▼
Generate Summary Report
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Core Development |
| OS Module | File and Directory Operations |
| Hashlib | MD5 Checksum Generation |

---

## 📂 Project Structure

```text
Duplicate-File-Remover/
│
├── DuplicateRemover.py
├── README.md
│
└── SampleDirectory/
    ├── file1.txt
    ├── file2.txt
    └── duplicate_file1.txt
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/duplicate-file-remover.git

cd duplicate-file-remover
```

### Verify Python Installation

```bash
python --version
```

Expected Output:

```bash
Python 3.x.x
```

---

## ▶️ Usage

Run the script:

```bash
python DuplicateRemover.py
```

Enter the directory name when prompted:

```text
Enter Directory Name : DemoFolder
```

The script will scan the directory and automatically remove duplicate files.

---

## 📊 Sample Output

```text
Enter Directory Name : DemoFolder

Deleted file : DemoFolder/copy_file1.txt
Deleted file : DemoFolder/copy_file2.txt

Total deleted files : 2
```

---

## 🔍 How It Works

### Step 1: Scan Directory

The script recursively traverses the specified directory using:

```python
os.walk()
```

### Step 2: Generate Checksums

Each file is processed using MD5 hashing:

```python
hashlib.md5()
```

### Step 3: Detect Duplicates

Files with identical MD5 checksums are considered duplicates.

### Step 4: Remove Duplicate Files

The script keeps one original copy and removes all additional duplicate files.

---

## 📈 Time Complexity

| Operation | Complexity |
|------------|------------|
| Directory Traversal | O(n) |
| Hash Generation | O(file size) |
| Duplicate Detection | O(n) |

Where **n** is the number of files in the directory.

---

## 🔒 Limitations

- Uses MD5 hashing (small possibility of collisions)
- Deleted files cannot be recovered automatically
- No confirmation prompt before deletion

---

## 🚧 Future Enhancements

- GUI Application using Tkinter
- SHA-256 Hash Support
- Duplicate Preview Before Deletion
- Restore Deleted Files Option
- Detailed Log File Generation
- Email Notification Support
- Multi-threaded Scanning
- Storage Statistics Dashboard

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python File Handling
- Directory Traversal
- Hashing Algorithms
- Dictionary Data Structures
- Automation Scripting
- Storage Optimization Techniques

---

## 👨‍💻 Author

**Shubham Pawar**

Python Developer | Data Analyst | Software Developer | UI/UX Designer

GitHub: https://github.com/Shub712

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
