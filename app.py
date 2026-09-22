import streamlit as st
import os
import google.generativeai as genai

st.set_page_config(page_title="Jarvis Live Search", layout="wide")
st.title("💼 Jarvis - Autonomous Job Scout")

# API Key load karna
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')

if st.button("Run Real Job Search"):
    if not api_key:
        st.error("API Key missing! Check Render environment variables.")
    else:
        with st.spinner("Jarvis is searching LinkedIn and live portals..."):
            prompt = "Find 3 real current job openings in India for Pharma Data Analyst or Clinical Data Manager requiring Python, SQL, and Power BI. Give output in a clean table."
            response = model.generate_content(prompt)
            st.markdown(response.text)
