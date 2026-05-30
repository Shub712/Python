# 🤖 Mini GPT From Scratch using TensorFlow

## 📌 Overview

This project implements a **Mini GPT (Generative Pre-trained Transformer)** from scratch using **TensorFlow and Keras**. The model demonstrates the core concepts behind modern Large Language Models (LLMs) such as GPT by implementing:

- Text Tokenization
- Token Embeddings
- Positional Embeddings
- Masked Self-Attention
- Decoder-Only Transformer Architecture
- Next Word Prediction
- Autoregressive Text Generation

The objective of this project is educational: to understand how GPT-style models work internally without relying on pre-trained models or external frameworks.

---

## 🚀 Features

- Build a GPT-style Decoder-Only Transformer from scratch
- Custom Token and Positional Embedding Layer
- Custom Causal Mask Implementation
- Multi-Head Self-Attention Mechanism
- Feed Forward Neural Network
- Residual Connections and Layer Normalization
- Next Word Prediction
- Autoregressive Text Generation
- TensorFlow/Keras Implementation
- Fully Explainable Educational Code

---

## 🧠 Concepts Covered

### Natural Language Processing (NLP)

- Tokenization
- Vocabulary Creation
- Word Embeddings
- Sequence Modeling

### Transformer Architecture

- Self-Attention
- Multi-Head Attention
- Positional Encoding
- Causal Masking
- Decoder-Only Transformer

### GPT Fundamentals

- Next Token Prediction
- Autoregressive Generation
- Context Understanding
- Language Modeling

---

## 🏗️ Architecture

```text
Input Text
     │
     ▼
Text Vectorization
     │
     ▼
Token Embeddings
     │
     ▼
Positional Embeddings
     │
     ▼
Transformer Decoder Block
     │
     ▼
Transformer Decoder Block
     │
     ▼
Dense Softmax Layer
     │
     ▼
Next Token Prediction
```

---

## 📂 Dataset

A small custom educational dataset is used containing sentences related to:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Transformers
- GPT Models
- NLP Concepts

Example:

```text
i love artificial intelligence
machine learning is powerful
gpt is decoder only transformer
language model predicts next word
```

---

## ⚙️ Model Configuration

| Parameter | Value |
|------------|---------|
| Vocabulary Size | 1000 |
| Sequence Length | 6 |
| Embedding Dimension | 32 |
| Attention Heads | 2 |
| Feed Forward Dimension | 64 |
| Epochs | 300 |
| Batch Size | 2 |
| Optimizer | Adam |
| Loss Function | Sparse Categorical Crossentropy |

---

## 🔒 Causal Masking

GPT models must not look at future words during training.

Example:

```text
Position 0 → Can see 0
Position 1 → Can see 0,1
Position 2 → Can see 0,1,2
Position 3 → Can see 0,1,2,3
```

Future tokens remain hidden.

This is achieved using a **Causal Attention Mask**.

---

## 📈 Training Objective

The model learns to predict the next word in a sequence.

Example:

Input:

```text
i love artificial
```

Target:

```text
love artificial intelligence
```

This is the same fundamental learning objective used in GPT models.

---

## 🔍 Next Word Prediction

The trained model can predict the next word given a partial sentence.

Example:

```python
predict_next_word("machine learning is")
```

Output:

```text
powerful
```

---

## ✨ Text Generation

The model supports autoregressive text generation.

Example:

```python
generate_text("i love", number_of_words=4)
```

Possible Output:

```text
i love artificial intelligence is future
```

---

## 📦 Requirements

### Python

```text
Python 3.10+
```

### Required Libraries

Create a file named `requirements.txt`

```txt
tensorflow>=2.12.0
numpy>=1.24.0
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install tensorflow numpy
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/mini-gpt-from-scratch.git

cd mini-gpt-from-scratch
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python MiniGPT_Industry_Commented.py
```

---

## 📁 Project Structure

```text
Mini-GPT-From-Scratch/
│
├── MiniGPT_Industry_Commented.py
├── requirements.txt
├── README.md
│
└── model_training_output/
```

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

- How GPT models tokenize text
- How embeddings work
- Why positional information is necessary
- How self-attention works
- Why causal masking is important
- How decoder-only transformers generate text
- How autoregressive generation works

---

## 🔮 Future Improvements

- Larger Training Dataset
- Byte Pair Encoding (BPE)
- Transformer Scaling
- Multiple Decoder Layers
- Temperature Sampling
- Top-K Sampling
- Top-P Sampling
- Model Checkpoint Saving
- Fine-Tuning Support
- Chatbot Interface
- Web Deployment using Flask/FastAPI

---

## 👨‍💻 Author

### Shubham Pawar

Aspiring Software Developer | Machine Learning Enthusiast | AI Learner

---

## 📚 References

- Attention Is All You Need (2017)
- GPT: Generative Pre-trained Transformer
- TensorFlow Documentation
- Keras Documentation

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub and sharing it with other AI enthusiasts.
