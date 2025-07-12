# summarizer.py

import os
import requests
import streamlit as st  # for accessing Streamlit secrets

# Load Gemini API key from Streamlit secrets
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# Gemini 2.0 Flash endpoint
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def summarize_text(text: str) -> str:
    if not GEMINI_API_KEY:
        return "❌ API Key not set. Please set GEMINI_API_KEY in Streamlit secrets."

    word_count = len(text.split())

    # Strict prompt to ensure short summary
    prompt = (
        f"Summarize the following text very briefly. Ensure the summary is significantly shorter "
        f"than the original input. Avoid restating every detail:\n\n{text}"
    )

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
        # Send request to Gemini API
        response = requests.post(
            GEMINI_URL,
            headers=headers,
            json=payload
        )

        if response.status_code != 200:
            return f"❌ Gemini API Error: {response.status_code} - {response.text}"

        data = response.json()
        summary = data['candidates'][0]['content']['parts'][0]['text']

        # Ensure summary is actually shorter
        if len(summary.split()) >= word_count:
            summary = (
                "⚠️ Gemini's response was longer than the input. Please try rephrasing your input "
                "or reducing its length for a better result."
            )

        # Log input and summary for evaluation
        with open("summary_log.txt", "a", encoding="utf-8") as f:
            f.write("\n---\n")
            f.write(f"Input ({word_count} words):\n{text[:500]}\n\n")
            f.write("Summary:\n" + summary + "\n")

        return summary

    except Exception as e:
        return f"❌ Error during summarization: {str(e)}"
