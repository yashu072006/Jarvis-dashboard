import os
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Jarvis - Job Scout", page_icon="💼")

st.title("💼 Jarvis - Autonomous Job Scout")
st.write("Automated Job Search Engine powered by Gemini")

# Configure Gemini API
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY environment variable missing in Render!")
else:
    genai.configure(api_key=api_key)

if st.button("Run Real Job Search"):
    with st.spinner("Scouting jobs..."):
        try:
            # Using stable model version
            model = genai.GenerativeModel('gemini-2.0-flash')
            
            prompt = (
                "Search and list top current job openings for Data Analytics and "
                "Pharmaceutical roles in India. Provide job title, company, location, "
                "and key requirements in a clean Markdown format."
            )
            
            response = model.generate_content(prompt)
            st.success("Search Complete!")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Error: {e}")
