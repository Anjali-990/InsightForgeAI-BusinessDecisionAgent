import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.helpers import load_data
from agents.sales_dashboard import show_sales_dashboard
from agents.hr_dashboard import show_hr_dashboard
from agents.finance_dashboard import show_finance_dashboard
from agents.marketing_dashboard import show_marketing_dashboard



# FIRST STREAMLIT COMMAND
st.set_page_config(page_title="InsightForge AI", layout="wide")

st.title("🧠 InsightForge AI")

st.markdown("""
### Business Decision Intelligence Agent

Transforming business data into actionable decisions through
multi-step reasoning, anomaly detection, and Microsoft Fabric IQ concepts.
""")

st.sidebar.title("InsightForge AI")

st.sidebar.info("""
Business Decision Intelligence Agent

Microsoft Agents League Hackathon 2026
""")


uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:

    # Load data
    df = load_data(uploaded_file)

    st.success("File uploaded successfully!")

    st.dataframe(df)

    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    # -----------------------------
    # Simple Dataset Detection
    # -----------------------------
    columns = [col.lower() for col in df.columns]

    if "sales" in columns:
        dataset_type = "sales"

    elif "salary" in columns:
        dataset_type = "hr"

    elif "revenue" in columns:
        dataset_type = "finance"

    elif "clicks" in columns:
        dataset_type = "marketing"

    else:
        dataset_type = "unknown"

    st.info(f"📂 Dataset Type Detected: {dataset_type.upper()}")

    analyze = st.button("🚀 Analyze Business Data")

    if analyze:
        st.session_state["analyzed"] = True

    if st.session_state.get("analyzed", False):

        if dataset_type == "sales":
            show_sales_dashboard(df)

        elif dataset_type == "hr":
            show_hr_dashboard(df)

        elif dataset_type == "finance":
            show_finance_dashboard(df)

        elif dataset_type == "marketing":
            show_marketing_dashboard(df)

        else:
            st.error("⚠️ Unknown dataset type. Please upload a valid Sales, HR, Finance, or Marketing dataset.")
    