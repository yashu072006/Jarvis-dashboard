import streamlit as st
import pandas as pd

st.set_page_config(page_title="Jarvis AI Agent", layout="wide")

st.title("🤖 Jarvis - AI Autonomous Agent")
st.sidebar.header("Navigation")
menu = st.sidebar.radio("Select Task", ["LinkedIn Automation", "YouTube Automation", "System Status"])

if menu == "LinkedIn Automation":
    st.header("💼 LinkedIn Job Search & Management")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Search Parameters")
        roles = st.text_input("Target Roles", "Data Analyst, Clinical Data Manager, Health Data Analyst")
        location = st.text_input("Location", "India / Remote")
        keywords = st.text_input("Keywords", "Python, SQL, Power BI, Pharma")
        
        if st.button("Run Job Search"):
            st.success(f"Searching jobs for: {roles} in {location}...")
            # Sample structure for job search
            jobs = [
                {"Title": "Data Analyst - Pharma", "Company": "Novartis", "Location": "Hyderabad (Hybrid)", "Match": "95%"},
                {"Title": "Clinical Data Analyst", "Company": "IQVIA", "Location": "Remote", "Match": "90%"},
                {"Title": "Health Data Engineer", "Company": "Target", "Location": "Bangalore", "Match": "85%"},
            ]
            df = pd.DataFrame(jobs)
            st.table(df)

elif menu == "YouTube Automation":
    st.header("🎥 YouTube Interaction")
    st.info("YouTube Automation module active. Connect API keys to start auto-engagement.")

elif menu == "System Status":
    st.header("⚡ System Health & Logs")
    st.success("Server Status: Online (Render Cloud)")
    st.write("24/7 Monitoring Active.")
