# 📚 AI Exam Prep Chatbot

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Gemini AI](https://img.shields.io/badge/Gemini%20AI-1.5%20Pro-blue)](https://ai.google.dev/)

**Exam Prep Chatbot** is an intelligent web application designed to help students master any subject through active recall. By leveraging the **Google Gemini 1.5 Pro** model, the chatbot generates high-quality, randomized flashcards tailored to specific user-input topics.



---

## ✨ Key Features

* **Intelligent Flashcard Generation:** Automatically creates 5 distinct "Question & Answer" pairs using Generative AI.
* **Dynamic Variation:** Uses a randomized seed and timestamp logic in prompt engineering to ensure content remains fresh and unique even for the same topic.
* **Fallback Logic:** Includes a robust backend verification loop to ensure exactly 5 flashcards are delivered, re-triggering the AI if the initial response is incomplete.
* [cite_start]**Responsive UI:** A modern, grid-based dashboard built with HTML5/CSS3 featuring clean animations and mobile-friendly design[cite: 1].

---

## 🛠️ Technical Stack

* **Backend:** Flask (Python)
* **AI Engine:** Google Generative AI (Gemini 1.5 Pro)
* [cite_start]**Frontend:** Jinja2, HTML5, CSS3 [cite: 1]
* **Deployment:** Configured for `gunicorn` to ensure stable production hosting.

---

## 📂 Repository Structure

| File | Description |
| :--- | :--- |
| `app.py` | Flask server handling routing and frontend-backend communication. |
| `chatbot.py` | AI integration layer handling API calls and prompt engineering. |
| `index.html` | [cite_start]The main UI template with dynamic flashcard rendering logic[cite: 1]. |
| `requirements.txt` | Dependency list (Flask, google-generativeai, gunicorn). |

---

## 🚀 Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/hkhimanshu3214/exam-prep-chatbot.git](https://github.com/hkhimanshu3214/exam-prep-chatbot.git)
    cd exam-prep-chatbot
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key:**
    Obtain a Gemini API key from Google AI Studio and set it in your environment:
    ```bash
    export GEMINI_API_KEY="your_api_key_here"
    ```

4.  **Run the Application:**
    ```bash
    python app.py
    ```
    Access the app at `http://127.0.0.1:5000`.

---

## 👥 Meet the Creators

* [cite_start]**Himanshu Fulera** (hkhimanshu3214@gmail.com) [cite: 1]
* [cite_start]**Ayush Yadav** (ayushyadav@gmail.com) [cite: 1]
* [cite_start]**Manish Jantwal** (manishjantwal21@gmail.com) [cite: 1]

---
Developed as a tool to help students prepare for exams efficiently. 🎓
