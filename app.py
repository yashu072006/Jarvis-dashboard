import streamlit as st
import pandas as pd
import plotly.express as px

# Mobile-first page settings
st.set_page_config(
    page_title="Jarvis Control Center",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark Theme
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #00D4FF; color: black; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Dashboard Title
st.title("⚡ Jarvis Control Center")
st.caption("Personal Mobile Dashboard")

# File Upload Section
uploaded_file = st.file_uploader("Upload CSV ya Excel File", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("Data load ho gaya!")

        # Key Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Rows", len(df))
        with col2:
            st.metric("Total Columns", len(df.columns))
        with col3:
            st.metric("Missing Values", df.isnull().sum().sum())

        st.divider()

        # Visualizations
        st.subheader("📊 Interactive Charts")
        
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

        if numeric_cols and categorical_cols:
            cat_col = st.selectbox("Category Select Karo (X-Axis):", categorical_cols)
            num_col = st.selectbox("Number Select Karo (Y-Axis):", numeric_cols)
            
            fig = px.bar(
                df, x=cat_col, y=num_col, 
                title=f"{num_col} vs {cat_col}",
                template="plotly_dark"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Chart ke liye numbers aur text dono data mein hona chahiye.")

        # Data Preview
        with st.expander("🔍 View Table"):
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("👉 Koi bhi CSV ya Excel file upload karke check karo!")
