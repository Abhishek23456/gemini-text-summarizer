# 🧠 Gemini Text Summarizer

A Streamlit web application that summarizes long text or articles using **Google Gemini 2.0 Flash API**.

---

## 🚀 Live Demo

👉 [Try it here](https://gemini-text-summarizer-8u6p4zk64hwv6gwvm4acdr.streamlit.app/)

> 🔐 Make sure to set your own Gemini API key in `.env` (for local use) or Streamlit Cloud Secrets (for deployment).

---

## 📌 Features

- 🔎 Summarizes text using Google's Gemini LLM (Flash 2.0)
- ⚡ Simple, clean UI with [Streamlit](https://streamlit.io)
- 🔐 API key handled securely (via `st.secrets`)
- ☁️ Deployed live using Streamlit Cloud

---

## 🛠️ Tech Stack

- Python 3
- Streamlit
- Requests
- Google Gemini API (Flash 2.0)
- python-dotenv (for local environment)

---

## 🧠 Approach

1. **Frontend**:
   - Built with [Streamlit](https://streamlit.io)
   - Clean layout with a text box and "Summarize" button

2. **Backend/Logic**:
   - When the user submits text, it sends a prompt to the **Gemini API** using an HTTP POST request.
   - Model used: `gemini-2.0-flash` via `https://generativelanguage.googleapis.com`
   - API key is stored securely via Streamlit Cloud’s **Secrets Manager**
     
---

## ⚙️ Setup Instructions

### ✅ Local Setup

1. Clone the repo
2. Install dependencies :pip install -r requirements.txt
3. Create .env file (for local testing) to store API key.
4. Run the app : streamlit run app.py
   
## 🌐 Hosting on Streamlit Cloud
If you want to deploy:

1. Push your code to a public GitHub repo
2. Go to Streamlit Cloud
3. Create a new app
4. Set the main file path as app.py
5. In the Secrets tab, add: GEMINI_API_KEY = "your_api_key_here"
