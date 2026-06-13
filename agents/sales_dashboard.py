import streamlit as st
import matplotlib.pyplot as plt

from agents.analyzer import detect_anomalies
from agents.reasoning import generate_reasoning
from agents.recommendations import generate_recommendations
from agents.executive_summary import generate_summary
from agents.fabric_iq import generate_fabric_iq
from agents.simulator import simulate_sales

from agents.report_generator import generate_sales_report

def show_sales_dashboard(df):
    st.header("📊 Sales Analysis")
    st.write("## Analysis Started")

    total_sales = df["Sales"].sum()
    avg_sales = df["Sales"].mean()
    total_customers = df["Customers"].sum()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💰 Total Sales", f"{total_sales:,.0f}")

    with col2:
        st.metric("📈 Average Sales", f"{avg_sales:,.0f}")

    with col3:
        st.metric("👥 Customers", f"{total_customers:,.0f}")

    st.success("Basic analysis completed!")



    # Sales by Region Chart
    st.header("📊 Sales Performance by Region")

    sales_by_region = df.groupby("Region")["Sales"].sum()

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(
        sales_by_region.index,
        sales_by_region.values
    )

    ax.set_xlabel("Region")
    ax.set_ylabel("Sales")
    ax.set_title("Sales by Region")

    st.pyplot(fig)

    # Inventory by Region
    st.header("📦 Inventory by Region")

    inventory = df.groupby("Region")["Inventory"].sum()

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        inventory.index,
        inventory.values
    )

    ax.set_xlabel("Region")
    ax.set_ylabel("Inventory")
    ax.set_title("Inventory by Region")

    st.pyplot(fig)

    #Customers by Region
    st.header("👥 Customers by Region")

    customers = df.groupby("Region")["Customers"].sum()

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        customers.index,
        customers.values
    )

    ax.set_xlabel("Region")
    ax.set_ylabel("Customers")
    ax.set_title("Customers by Region")

    st.pyplot(fig)

    # Business Health Dashboard
    st.header("📈 Business Health Dashboard")

    col1, col2, col3 = st.columns(3)

    sales_change = (
        (df["Sales"].iloc[-1] - df["Sales"].iloc[0])
        / df["Sales"].iloc[0]
    ) * 100

    inventory_change = (
        (df["Inventory"].iloc[-1] - df["Inventory"].iloc[0])
        / df["Inventory"].iloc[0]
    ) * 100

    customer_change = (
        (df["Customers"].iloc[-1] - df["Customers"].iloc[0])
        / df["Customers"].iloc[0]
    ) * 100

    with col1:
        st.metric(
            "Sales Trend",
            f"{sales_change:.1f}%"
        )

    with col2:
        st.metric(
            "Inventory Trend",
            f"{inventory_change:.1f}%"
    )

    with col3:
        st.metric(
            "Customer Trend",
            f"{customer_change:.1f}%"
        )

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
    total_sales = df["Sales"].sum()
    summary = generate_summary(total_sales)
    
    report = generate_sales_report(summary)

    st.download_button(
    label="⬇ Download Sales Report",
    data=report,
    file_name="Sales_Report.txt",
    mime="text/plain"
    )

    st.text_area(
            "Business Summary",
            summary,
            height=255

        )
# Adding - "Microsoft Fabric IQ Reasoning" 
    st.header("🧠 Microsoft Fabric IQ Reasoning")

    entities, relationships, risk = generate_fabric_iq(df)

    st.subheader("Business Entities")

    for entity in entities:
        st.success(entity)

    st.subheader("Relationships Discovered")

    if relationships:
        for relation in relationships:
            st.info(relation)

    else:
        st.success("No significant business relationships detected.")

    st.subheader("Business Risk")
    if risk == "High":
        st.error("🔴 High Risk")

    elif risk == "Medium":
        st.warning("🟡 Medium Risk")

    else:
        st.success("🟢 Low Risk")
            
    st.write(
        """
        Fabric IQ reasoning evaluates   relationships between
        business entities such as customers, inventory,
        sales, and regions to identify risks and recommend actions.
        """
    )


    #   What-if Simultor 
    st.write("## What-If Simulator")

    inventory_increase = st.number_input(
        "Increase Inventory By (%)",
        min_value=0,
        max_value=100,
        value=10
    )

    if st.button("Run Simulation",key="sales_simulation_button"):

        current_sales = df["Sales"].sum()

        predicted_sales, improvement = simulate_sales(
            current_sales,
            inventory_increase
        )

        st.write("### Simulation Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Current Sales",
                f"{current_sales:,.0f}"
            )

        with col2:
            st.metric(
                "Predicted Sales",
                f"{predicted_sales:,.0f}"
        )

        with col3:
            st.metric(
                "Estimated Improvement",
                f"{improvement:,.0f}"
            )

        st.success(
            f"Based on a simplified business model, a {inventory_increase}% increase in inventory may support higher sales if demand remains stable."
        )

    st.markdown("---")
    st.caption("Built for Microsoft Agents League Hackathon 2026")


