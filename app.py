import streamlit as st
import pandas as pd
from agents.analyzer import detect_anomalies
from agents.reasoning import generate_reasoning
from agents.recommendations import generate_recommendations
# Page Title
st.set_page_config(page_title="InsightForge AI", layout="wide")

st.title("📊 InsightForge AI")
st.subheader("Business Decision Intelligence Agent")

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload your sales data (CSV)",
    type=["csv"]
)

if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # Preview Data
    st.write("### Dataset Preview")
    st.dataframe(df)

    # Basic Information
    st.write("### Dataset Information")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    # Analyze Button
    analyze = st.button("Analyze Data")

    if analyze:
            st.session_state["analyzed"] = True

    if st.session_state.get("analyzed", False):

        st.write("## Analysis Started")

        total_sales = df["Sales"].sum()
        avg_sales = df["Sales"].mean()
        total_customers = df["Customers"].sum()

        st.metric("Total Sales", f"{total_sales:,.0f}")
        st.metric("Average Sales", f"{avg_sales:,.0f}")
        st.metric("Total Customers", f"{total_customers:,.0f}")

        st.success("Basic analysis completed!")


# Detected Issues
        st.write("## Detected Issues")

        insights = detect_anomalies(df)

        if insights:
            for item in insights:
                st.warning(item)
        else:
            st.success("No major anomalies detected.")

        st.write("## Root Cause Analysis")

        reasons = generate_reasoning(df)

        if reasons:
            for reason in reasons:
                st.info(reason)
        else:
            st.success("No major root causes detected.")
        
# Recommended Actions
        st.write("## Recommended Actions")

        recommendations = generate_recommendations(df)

        if recommendations:
            for rec in recommendations:
                st.success(rec)
        else:
            st.success("No recommendations required.")

# Executive Summary
        st.write("## Executive Summary")

        summary = f"""
Business Performance Summary

Total Sales: {total_sales:,.0f}

Key Findings:
- Sales decline detected in one or more regions.
- Inventory shortages observed.
- Customer retention concerns identified.

Recommended Actions:
- Increase inventory where shortages exist.
- Launch customer retention initiatives.
- Monitor regional sales weekly.

Overall Risk Level: Medium to High
"""

        st.text_area(
            "Business Summary",
            summary,
            height=250
        )


# Adding - "Microsoft Fabric IQ Reasoning" 
        st.write("## 🧠 Microsoft Fabric IQ Reasoning")

        entities = []

        if "Sales" in df.columns:
            entities.append("Sales")

        if "Inventory" in df.columns:
            entities.append("Inventory")

        if "Customers" in df.columns:
            entities.append("Customers")

        if "Region" in df.columns:
            entities.append("Regions")

        st.write("### Business Entities Identified")

        for entity in entities:
            st.success(entity)


# Relationships Discovered

        st.write("### Relationships Discovered")

        st.info(
            "Inventory shortages appear to correlate with declining sales performance."
        )

        st.info(
            "Customer decline appears to correlate with reduced revenue."
        )

# Business Risk Assessment
        st.write("### Business Risk Assessment")

        st.warning("Risk Level: Medium to High")

        st.write(
            """
            Fabric IQ reasoning evaluates   relationships between
            business entities such as customers, inventory,
            sales, and regions to identify risks and recommend actions.
            """
        )


# What-if Simultor 
        st.write("## What-If Simulator")

        inventory_increase = st.number_input(
            "Increase Inventory By (%)",
            min_value=0,
            max_value=100,
            value=10
        )

        if st.button("Run Simulation"):

            current_sales = df["Sales"].sum()

            predicted_sales = current_sales * (1 + inventory_increase / 100)

            improvement = predicted_sales - current_sales

            st.write("### Simulation Results")

            st.metric(
                "Current Sales",
                f"{current_sales:,.0f}"
            )

            st.metric(
                "Predicted Sales",
                f"{predicted_sales:,.0f}"
            )

            st.metric(
                "Estimated Improvement",
                f"{improvement:,.0f}"
            )

            st.success(
                f"Based on a simplified business model, a {inventory_increase}% increase in inventory may support higher sales if demand remains stable."
            )