# 🔍 Industrial Surface Crack Detection using CNN

## 📌 Project Overview

This project implements an Industrial Surface Crack Detection System using Deep Learning (Convolutional Neural Networks - CNN). The model automatically classifies industrial surface images into two categories:

- Crack (Defective Surface)
- No Crack (Non-Defective Surface)

The system is designed to assist quality control and inspection processes in manufacturing and construction industries by reducing manual inspection efforts and improving defect detection accuracy.

---

## 🚀 Features

- Automated surface crack detection using Deep Learning
- Dataset preprocessing and validation
- Automatic Train / Validation / Test dataset splitting
- Image augmentation for improved generalization
- Multi-layer CNN architecture with Batch Normalization
- Early Stopping and Learning Rate Scheduling
- Model Checkpointing
- Performance evaluation using Accuracy, Loss, Confusion Matrix, and Classification Report
- Single Image Prediction Support
- Model Export for Deployment

---

## 📂 Dataset Structure

Place your dataset in the following format:

```text
CrackDataset/
│
├── Positive/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
│
└── Negative/
    ├── image1.jpg
    ├── image2.jpg
    └── ...
```

### Dataset Classes

| Folder | Description |
|----------|-------------|
| Positive | Images containing cracks |
| Negative | Images without cracks |

---

## 🏗️ Project Workflow

```text
Raw Dataset
     │
     ▼
Dataset Validation
     │
     ▼
Train / Validation / Test Split
     │
     ▼
Image Augmentation
     │
     ▼
CNN Model Training
     │
     ▼
Performance Evaluation
     │
     ▼
Model Saving
     │
     ▼
Single Image Prediction
```

---

## 🧠 CNN Architecture

```text
Input Image (128x128x3)
        │
        ▼
Conv2D (32) + BatchNormalization + MaxPooling
        │
        ▼
Conv2D (64) + BatchNormalization + MaxPooling
        │
        ▼
Conv2D (128) + BatchNormalization + MaxPooling
        │
        ▼
Conv2D (256) + BatchNormalization + MaxPooling
        │
        ▼
Flatten
        │
        ▼
Dense (256) + Dropout
        │
        ▼
Dense (128) + Dropout
        │
        ▼
Dense (1) Sigmoid Output
```

---

## ⚙️ Hyperparameters

| Parameter | Value |
|------------|--------|
| Image Size | 128 × 128 |
| Batch Size | 32 |
| Epochs | 15 |
| Optimizer | Adam |
| Loss Function | Binary Crossentropy |
| Output Activation | Sigmoid |
| Random Seed | 42 |

---

## 📊 Data Augmentation

The following augmentation techniques are applied during training:

- Rotation (15°)
- Zoom (20%)
- Width Shift
- Height Shift
- Horizontal Flip
- Image Rescaling

These transformations improve model robustness and reduce overfitting.

---

## 📈 Evaluation Metrics

The model is evaluated using:

- Test Accuracy
- Test Loss
- Confusion Matrix
- Precision
- Recall
- F1 Score
- Classification Report

---

## 💾 Generated Models

After training, the following files are generated:

```text
Best_Crack_Detection_Model.keras
Final_Marvellous_Crack_Detection_Model.keras
```

---

## 🔍 Single Image Prediction

The application includes a utility function for predicting individual images.

### Output

```text
Crack Detected
```

or

```text
No Crack
```

---

## 📦 Requirements

### Python Version

```text
Python 3.10+
```

### Required Libraries

Create a `requirements.txt` file:

```txt
tensorflow>=2.12.0
numpy>=1.24.0
matplotlib>=3.7.0
scikit-learn>=1.3.0
pillow>=10.0.0
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install tensorflow numpy matplotlib scikit-learn pillow
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/industrial-surface-crack-detection.git

cd industrial-surface-crack-detection
```

### Run Project

```bash
python crack_detection.py
```

---

## 📁 Project Structure

```text
Industrial-Surface-Crack-Detection/
│
├── CrackDataset/
│   ├── Positive/
│   └── Negative/
│
├── Processed_CrackDataset/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── crack_detection.py
├── requirements.txt
├── README.md
│
├── Best_Crack_Detection_Model.keras
└── Final_Marvellous_Crack_Detection_Model.keras
```

---

## 🎯 Applications

- Manufacturing Quality Inspection
- Industrial Defect Detection
- Infrastructure Monitoring
- Concrete Crack Analysis
- Road Surface Inspection
- Bridge Health Monitoring
- Predictive Maintenance Systems

---

## 🔮 Future Enhancements

- Transfer Learning (ResNet50, EfficientNet)
- Real-Time Video Crack Detection
- Flask/Django Web Deployment
- Mobile Application Integration
- Multi-Class Defect Detection
- Explainable AI using Grad-CAM

---

## 👨‍💻 Author

**Shubham Pawar**

Aspiring Software Developer | Data Analytics Enthusiast | Machine Learning Learner

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
