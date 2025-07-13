# app.py
import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="Gemini Text Summarizer")
st.title("Text Summarizer using Gemini")

st.markdown("Paste any text or article below and get a summary using **Gemini LLM**.")

user_input = st.text_area("Enter Article/Text Here", height=300)

if st.button("Summarize"):
    with st.spinner("Calling Gemini LLM..."):
        summary = summarize_text(user_input)
    st.subheader("🔍 Summary:")
    st.success(summary)
