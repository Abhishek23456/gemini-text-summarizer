# Gemini Text Summarizer

This is a web-based AI utility tool that summarizes long articles or text inputs using **Google Gemini 2.0 Flash** via its API. It features a simple and intuitive interface built using **Streamlit** and is deployed using **Streamlit Cloud** for public access.

---

## 🔍 Objective

To build a lightweight, real-world utility tool that can:
- Accept user input (text or article)
- Call the **Gemini 2.0 Flash API** to generate a smart summary
- Display the summarized output in an elegant interface

---

## 🧠 Approach

1. **Frontend**:
   - Built with [Streamlit](https://streamlit.io)
   - Clean layout with a text box and "Summarize" button

2. **Backend/Logic**:
   - When the user submits text, it sends a prompt to the **Gemini API** using an HTTP POST request.
   - Model used: `gemini-2.0-flash` via `https://generativelanguage.googleapis.com`
   - API key is stored securely via Streamlit Cloud’s **Secrets Manager**

3. **Logging**:
   - All inputs and generated summaries are logged to `summary_log.txt` for reference and evaluation.

---

## 🌐 Live App

✅ Try it here: [Gemini Text Summarizer](https://gemini-text-summarizer-b9my4jeye3j6syoz2f2lmw.streamlit.app/)

---

## ⚙️ Setup Instructions

### ✅ Local Setup

1. Clone the repo
2. Install dependencies : pip install -r requirements.txt
3. Create .env file (for local testing) : GEMINI_API_KEY=your_actual_key_here
4. Run the app : streamlit run app.py

## 🌐 Hosting on Streamlit Cloud
1. Push your code to a public GitHub repo
2. Go to Streamlit Cloud
3. Create a new app
4. Set the main file path as app.py
5. In the Secrets tab, add gemini api key.


## 🧪 Usage

### ✅ 1. Local Usage

Once the app is running locally (`streamlit run app.py`), it will open a browser window with the following interface:

#### 🖥️ Interface:
- A **text area** to paste or type any long text/article.
- A **"Summarize" button** to generate the summary.
- Below the button, the **summary result** is displayed.
- Optionally, logs are saved in `summary_log.txt`.

#### 🧪 Steps:
1. Paste any paragraph or article (e.g., from Wikipedia or a news site).
2. Click the **Summarize** button.
3. Wait a moment — the Gemini API will return a clean summary.
4. View the output on the same screen.

---

### 🌍 2. Streamlit Cloud Usage

The hosted version of the app works exactly the same:

🔗 Visit: [Gemini Text Summarizer](https://gemini-text-summarizer-b9my4jeye3j6syoz2f2lmw.streamlit.app/)

#### Steps:
1. Enter the text you want to summarize.
2. Click **Summarize**.
3. Get the summary instantly below.

---
