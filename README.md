# YOLO Image Classification - Bird, Cat, Dog 🐦🐱🐶

## 🚀 Project Overview
This repository contains an **image classification model using YOLO (You Only Look Once)** to classify images into three categories: **bird, cat, and dog**. The model has been trained, evaluated, and deployed on **Hugging Face Spaces** for easy access and testing.

## 📌 Features
- **YOLO-based image classification** for real-time predictions.
- **Interactive deployment** using Gradio on Hugging Face Spaces.

## 🛠️ Model Development Steps
### 1️⃣ Dataset Preparation
- Collected and preprocessed images of **birds, cats, and dogs**.
- Split the dataset into **training, validation, and testing sets**.
- Dataset can be downloaded here : https://www.kaggle.com/datasets/mahmoudnoor/high-resolution-catdogbird-image-dataset-13000

### 2️⃣ Training the YOLO Model
- Used **YOLO** for classification with custom training settings.
- Trained the model and saved the best checkpoint (`best.pt`).

### 3️⃣ Model Evaluation
- **Confusion Matrix Analysis**
  - **98% accuracy for birds**
  - **92% accuracy for cats** (with 8% misclassification to dogs)
  - **99% accuracy for dogs**
- **Loss and Accuracy Tracking**
  - Training loss reduced significantly over epochs.
  - Top-1 and Top-5 accuracy improved steadily.

### 4️⃣ Deployment on Hugging Face Spaces
- **Created a Gradio interface** for user-friendly interaction.
- **Pushed the model and interface** to Hugging Face Spaces for public access.

---
Made with ❤️ by **Helmy** 🚀
