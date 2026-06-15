# 🩺 Medinova AI - AI Powered Healthcare Assistant

Medinova AI is a healthcare platform that combines Artificial Intelligence, Machine Learning, and modern web technologies to provide smart healthcare assistance.

The platform helps users with disease prediction, medical report analysis, AI doctor conversations, and voice-based assistance.

---

##  Features

###  Disease Prediction
- Predicts possible diseases based on user symptoms.
- User enters health details like:
  - Fever
  - Cough
  - Fatigue
  - Difficulty breathing
  - Age
  - Gender
  - Blood pressure
  - Cholesterol level

- Uses a Machine Learning model trained with healthcare data.

---

###  Medical Report Analyzer

- Users can upload medical reports.
- AI analyzes the report and provides meaningful insights.
- Helps users understand medical information easily.

---

###  AI Doctor Chat

- AI-powered medical assistant for healthcare-related conversations.
- Uses Ollama with Llama 3.2 model for local AI responses.

---

###  Voice Assistant

- Supports voice-based interaction.
- Converts speech into text.
- Generates AI responses.
- Converts responses back into speech.

---

## 🏗️ Project Architecture

Frontend (React + Vite)
|
|
↓
Backend API (FastAPI)
|
|
├── Machine Learning Model
|
├── Report Analyzer
|
└── Ollama AI Model


---

## 🛠️ Tech Stack

### Frontend
- React.js
- Vite
- Axios
- React Router
- CSS

### Backend
- FastAPI
- Python
- Uvicorn

### Machine Learning
- Scikit-learn
- Pandas
- Joblib

### AI
- Ollama
- Llama 3.2

### Other
- PDF Processing
- Speech Recognition
- Text To Speech

---
🤖 Ollama Setup

Install Ollama and download model:

ollama pull llama3.2:3b

Start Ollama:

ollama serve

AI Doctor Chat will use the local Llama model.

🌐 Deployment

Frontend:

Deployed using Vercel  LIVE LINK----> (https://medinova-ai-chi.vercel.app/)

Backend:

Deployed using Render  

Machine Learning features:

Available online

AI Chat:

Runs locally using Ollama

🎯 Future Improvements
Add user authentication with database
Improve disease prediction accuracy
Add medical history tracking
Deploy AI model on cloud infrastructure
Add multilingual support

