import streamlit as st
import matplotlib.pyplot as plt

from agents.report_generator import generate_finance_report
def show_finance_dashboard(df):

    st.header("💰 Finance Analysis")

    st.write("## Financial Overview")

    # KPIs
    total_revenue = df["Revenue"].sum()
    total_expense = df["Expense"].sum()
    net_profit = total_revenue - total_expense
    profit_margin = (net_profit / total_revenue) * 100
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💵 Total Revenue",
            f"{total_revenue:,.0f}"
        )

    with col2:
        st.metric(
            "💸 Total Expense",
            f"{total_expense:,.0f}"
        )

    with col3:
        st.metric(
            "📈 Net Profit",
            f"{net_profit:,.0f}"
        )

    st.success("Finance analysis completed!")

# Revenue Chart
    st.header("📊 Revenue by Month")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(
        df["Month"],
        df["Revenue"],
        marker="o"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    ax.set_title("Revenue Trend")

    st.pyplot(fig)

# Expense Chart
    st.header("💸 Expense by Month")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(
        df["Month"],
        df["Expense"],
        marker="o"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Expense")
    ax.set_title("Expense Trend")

    st.pyplot(fig)

# Profit Trend
    st.header("📈 Monthly Profit")

    profit = df["Revenue"] - df["Expense"]

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        df["Month"],
        profit
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Profit")
    ax.set_title("Monthly Profit")

    st.pyplot(fig)


 # Financial Health

    st.header("📈 Financial Health")

    revenue_growth = (
        (df["Revenue"].iloc[-1] - df["Revenue"].iloc[0])
        / df["Revenue"].iloc[0]
    ) * 100

    expense_growth = (
        (df["Expense"].iloc[-1] - df["Expense"].iloc[0])
        / df["Expense"].iloc[0]
    ) * 100

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Revenue Growth",
            f"{revenue_growth:.1f}%"
        )

    with col2:
        st.metric(
            "Expense Growth",
            f"{expense_growth:.1f}%"
        )

    with col3:
        st.metric(
            "Profit Margin",
            f"{profit_margin:.1f}%"
        )

    
    # Financial Risk Detection

    st.header("🚨 Financial Risk Assessment")

    risks = []

    if profit_margin < 10:
        risks.append("⚠️ Profit margin is below 10%.")

    if expense_growth > revenue_growth:
        risks.append("⚠️ Expenses are growing faster than revenue.")

    if net_profit < 0:
        risks.append("🔴 Business is operating at a loss.")

    if risks:
        for risk in risks:
            st.warning(risk)
    else:
        st.success("No major financial risks detected.")

    # ==========================
    # AI Financial Reasoning
    # ==========================

    st.header("🧠 Financial Reasoning")

    reasons = []

    if expense_growth > revenue_growth:
        reasons.append(
            "Operational expenses are increasing faster than revenue growth, reducing overall profitability."
        )

    if profit_margin < 10:
        reasons.append(
            "Low profit margins indicate a need for cost optimization or revenue growth."
        )

    if revenue_growth > expense_growth:
        reasons.append(
            "Revenue growth is outpacing expenses, indicating healthy financial performance."
        )

    if reasons:
        for reason in reasons:
            st.info(reason)
    else:
        st.success("Financial indicators appear stable.")

    # ==========================
    # Recommendations
    # ==========================

    st.header("✅ Recommendations")

    recommendations = []

    if profit_margin < 10:
        recommendations.append(
            "Reduce operational costs to improve profitability."
        )

    if expense_growth > revenue_growth:
        recommendations.append(
            "Review high-expense departments and optimize spending."
        )

    if revenue_growth <= 5:
        recommendations.append(
            "Explore new revenue streams and customer acquisition strategies."
        )

    if not recommendations:
        recommendations.append(
            "Maintain current financial strategy while monitoring KPIs."
        )

    for rec in recommendations:
        st.success(rec)

    # ==========================
    # Executive Summary
    # ==========================

    st.header("📋 Executive Summary")

    if profit_margin >= 20:
        health = "Excellent"

    elif profit_margin >= 10:
        health = "Good"

    else:
        health = "Needs Improvement"

    summary = f"""
Finance Performance Summary

Total Revenue: {total_revenue:,.0f}

Total Expense: {total_expense:,.0f}

Net Profit: {net_profit:,.0f}

Profit Margin: {profit_margin:.1f}%

Financial Health: {health}

Key Findings

• Revenue Growth: {revenue_growth:.1f}%

• Expense Growth: {expense_growth:.1f}%

Recommended Actions

• Continue monitoring monthly financial KPIs.

• Optimize costs where possible.

• Improve revenue through business expansion.

Overall Financial Risk: {"High" if profit_margin < 10 else "Medium" if profit_margin < 20 else "Low"}
"""

    st.text_area(
        "Finance Report",
        summary,
        height=260
    )

    report = generate_finance_report(summary)

    st.download_button(
    label="⬇ Download Finance Report",
    data=report,
    file_name="Finance_Report.txt",
    mime="text/plain"
    )

    st.markdown("---")
    st.caption("Built for Microsoft Agents League Hackathon 2026")