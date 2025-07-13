# summarizer.py

import requests
import streamlit as st  # Needed for Streamlit Secrets

# Read API key from Streamlit secrets (set via cloud UI)
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# Gemini 2.0 Flash endpoint
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def summarize_text(text: str) -> str:
    if not GEMINI_API_KEY:
        return "❌ API Key not set. Please set GEMINI_API_KEY in Streamlit secrets."

    prompt = f"Summarize the following text:\n\n{text}"

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(
            GEMINI_URL,
            headers=headers,
            json=payload
        )

        if response.status_code != 200:
            return f"❌ Gemini API Error: {response.status_code} - {response.text}"

        data = response.json()
        summary = data['candidates'][0]['content']['parts'][0]['text']

        # Log result (optional)
        with open("summary_log.txt", "a", encoding="utf-8") as f:
            f.write("\n---\nInput:\n" + text[:500] + "\n\nSummary:\n" + summary + "\n")

        return summary

    except Exception as e:
        return f"❌ Error during summarization: {str(e)}"
