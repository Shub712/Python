# 🎯 Marvellous SmartHire AI Agent

## 🚀 Overview

Marvellous SmartHire AI Agent is an AI-powered Mock Interview System designed to simulate real-world technical interviews using Large Language Models (LLMs).

The application asks technical interview questions, evaluates candidate responses using Llama 3 through Ollama, assigns scores, provides detailed feedback, and generates a comprehensive interview performance report.

The project demonstrates practical implementation of AI Agents, Prompt Engineering, LLM Integration, Automated Evaluation Systems, and Report Generation using Python.

---

## ✨ Features

- 🤖 AI-Powered Mock Interview System
- 📝 Technical Question Evaluation
- 🧠 LLM Integration using Llama 3
- 🎯 Automated Scoring (0–10)
- 📊 Performance Analysis
- 📚 Topic-wise Interviews
- 🔍 Missing Concept Detection
- 💡 Improved Answer Suggestions
- 📄 Automated Report Generation
- 📁 Report Storage with Timestamps
- 🗂️ Interview History Tracking
- 🔄 Full Interview and Topic-wise Modes

---

## 🏗️ System Architecture

```text
Student
   │
   ▼
Interview Questions
   │
   ▼
AI Interview Agent
   │
   ▼
Prompt Engineering
   │
   ▼
Ollama API
   │
   ▼
Llama 3 Model
   │
   ▼
Answer Evaluation
   │
   ▼
Score Extraction
   │
   ▼
Performance Analysis
   │
   ▼
Final Interview Report
```

---

## 📂 Project Structure

```text
Marvellous-SmartHire-AI-Agent/
│
├── main.py
│   └── Application Entry Point
│
├── interview_agent.py
│   └── Core AI Interview Logic
│
├── llm_engine.py
│   └── Communication with Ollama & Llama3
│
├── report_generator.py
│   └── Interview Report Generation
│
├── questions.py
│   └── Technical Question Bank
│
├── reports/
│   └── Generated Interview Reports
│
├── requirements.txt
│
└── README.md
```

---

## 🧠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| Ollama | Local LLM Runtime |
| Llama 3 | Large Language Model |
| Requests | API Communication |
| Prompt Engineering | Structured Evaluation |
| Object-Oriented Programming | System Design |
| File Handling | Report Generation |

---

## 📋 Interview Topics Covered

### Python
- Lists
- Tuples
- Sets

### Object-Oriented Programming
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

### Machine Learning
- Supervised Learning
- Unsupervised Learning

### Deep Learning
- Activation Functions
- Neural Networks

### Transformer Architecture
- Self-Attention Mechanism

### Large Language Models
- GPT
- Llama
- Foundation Models

### Retrieval-Augmented Generation (RAG)
- Context Retrieval
- Knowledge Grounding

### AI Agents
- Agent Architecture
- Agent vs Chatbot

---

## ⚙️ How It Works

### Step 1: Start Interview

The candidate selects:

```text
1. Full Interview
2. Topic-wise Interview
3. Exit
```

### Step 2: Answer Questions

Example:

```text
Question:
What is a Large Language Model?

Answer:
A Large Language Model is a deep learning model trained on massive amounts of text data.
```

### Step 3: Prompt Generation

The AI Agent automatically creates a structured evaluation prompt containing:

- Student Name
- Topic
- Question
- Candidate Answer

### Step 4: LLM Evaluation

Llama 3 evaluates:

- Technical Accuracy
- Concept Understanding
- Completeness
- Communication Quality

### Step 5: Score Extraction

Example:

```text
Score: 8/10
```

### Step 6: Feedback Generation

The AI generates:

```text
Evaluation
Missing Points
Improved Answer
Interview Suggestion
```

### Step 7: Report Generation

The system generates a detailed report and stores it automatically in the reports folder.

---

## 📊 Performance Categories

| Average Score | Performance |
|--------------|-------------|
| 8 – 10 | Excellent |
| 6 – 7.99 | Good |
| 4 – 5.99 | Average |
| Below 4 | Needs Improvement |

---

## 📄 Sample Evaluation Output

```text
Score: 8/10

Evaluation:
The answer demonstrates a good understanding of the concept.

Missing Points:
The candidate should mention real-world applications.

Improved Answer:
Machine Learning is a subset of Artificial Intelligence
that enables systems to learn from data and make predictions
without being explicitly programmed.

Interview Suggestion:
Include practical examples to improve answer quality.
```

---

## 📑 Sample Generated Report

```text
Student Name : Shubham Pawar

Total Questions Asked : 8
Total Score           : 64
Average Score         : 8.0

Overall Performance:
Excellent Performance
```

---

## 📦 Requirements

### Python Version

```text
Python 3.10+
```

### requirements.txt

```txt
requests>=2.31.0
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Verify Installation

```bash
ollama --version
```

### Download Llama 3

```bash
ollama pull llama3
```

### Start Llama 3

```bash
ollama run llama3
```

---

## ▶️ Running the Project

```bash
python main.py
```

---

## 🎯 Concepts Demonstrated

- Artificial Intelligence
- AI Agents
- Prompt Engineering
- Large Language Models (LLMs)
- Interview Automation
- Object-Oriented Programming
- API Communication
- Automated Assessment Systems
- Report Generation
- Performance Analytics

---

## 💼 Applications

- Placement Preparation
- Technical Interview Practice
- Student Skill Assessment
- Training Institutes
- Campus Recruitment
- AI Learning Platforms
- Interview Readiness Evaluation

---

## 🔮 Future Enhancements

- Streamlit Web Dashboard
- Voice-Based Interviews
- Resume Analysis
- Coding Interview Evaluation
- HR Interview Simulation
- Multi-Language Support
- Database Integration
- PDF Report Export
- Candidate Analytics Dashboard
- Interview Performance Tracking

---

## 👨‍💻 Author

**Shubham Kiran Pawar**

Aspiring Software Developer | AI & Machine Learning Enthusiast

---

## 📜 License

This project is developed for educational, learning, and portfolio purposes.

Feel free to modify and extend it according to your requirements.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
