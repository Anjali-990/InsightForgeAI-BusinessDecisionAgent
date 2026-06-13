import streamlit as st
import matplotlib.pyplot as plt

from agents.report_generator import generate_marketing_report
def show_marketing_dashboard(df):

    st.header("📢 Marketing Analysis")
    st.write("## Marketing Campaign Overview")

    # ==========================
    # KPIs
    # ==========================

    total_campaigns = len(df)
    total_clicks = df["Clicks"].sum()
    total_impressions = df["Impressions"].sum()
    average_ctr = df["CTR"].mean()
    average_roi = df["ROI"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📢 Campaigns", total_campaigns)

    with col2:
        st.metric("👆 Clicks", f"{total_clicks:,}")

    with col3:
        st.metric("👀 Impressions", f"{total_impressions:,}")

    with col4:
        st.metric("💹 Avg ROI", f"{average_roi:.1f}%")

    st.success("Marketing analysis completed!")

    # ==========================
    # Clicks by Campaign
    # ==========================

    st.header("👆 Clicks by Campaign")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        df["Campaign"],
        df["Clicks"]
    )

    ax.set_xlabel("Campaign")
    ax.set_ylabel("Clicks")
    ax.set_title("Campaign Clicks")

    plt.xticks(rotation=20)

    st.pyplot(fig)

    # ==========================
    # CTR by Campaign
    # ==========================

    st.header("📈 CTR by Campaign")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(
        df["Campaign"],
        df["CTR"],
        marker="o"
    )

    ax.set_xlabel("Campaign")
    ax.set_ylabel("CTR (%)")
    ax.set_title("Click Through Rate")

    plt.xticks(rotation=20)

    st.pyplot(fig)

    # ==========================
    # ROI by Campaign
    # ==========================

    st.header("💰 ROI by Campaign")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        df["Campaign"],
        df["ROI"]
    )

    ax.set_xlabel("Campaign")
    ax.set_ylabel("ROI (%)")
    ax.set_title("Campaign ROI")

    plt.xticks(rotation=20)

    st.pyplot(fig)

    # ==========================
    # Marketing Health
    # ==========================

    st.header("📊 Marketing Health")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Average CTR",
            f"{average_ctr:.2f}%"
        )

    with col2:
        st.metric(
            "Average ROI",
            f"{average_roi:.2f}%"
        )

    # ==========================
    # Risk Assessment
    # ==========================

    st.header("🚨 Marketing Risk Assessment")

    risks = []

    if average_ctr < 5:
        risks.append("⚠️ Low average click-through rate detected.")

    if average_roi < 20:
        risks.append("⚠️ Campaign ROI is relatively low.")

    if risks:
        for risk in risks:
            st.warning(risk)
    else:
        st.success("No major marketing risks detected.")

    # ==========================
    # Marketing Reasoning
    # ==========================

    st.header("🧠 Marketing Reasoning")

    if average_ctr < 5:
        st.info(
            "Campaigns receive impressions but relatively few clicks, suggesting creatives or targeting may need improvement."
        )

    if average_roi < 20:
        st.info(
            "Marketing investment is generating limited returns. Campaign optimization is recommended."
        )

    if average_ctr >= 5 and average_roi >= 20:
        st.success(
            "Campaign engagement and return on investment indicate healthy marketing performance."
        )

    # ==========================
    # Recommendations
    # ==========================

    st.header("✅ Recommendations")

    if average_ctr < 5:
        st.success("Improve ad creatives and audience targeting.")

    if average_roi < 20:
        st.success("Focus budget on high-performing campaigns.")

    if average_ctr >= 5 and average_roi >= 20:
        st.success("Maintain current campaign strategy.")

    # ==========================
    # Executive Summary
    # ==========================

    st.header("📋 Executive Summary")

    summary = f"""
Marketing Performance Summary

Campaigns: {total_campaigns}

Total Clicks: {total_clicks:,}

Total Impressions: {total_impressions:,}

Average CTR: {average_ctr:.2f}%

Average ROI: {average_roi:.2f}%

Key Findings

• Campaign engagement evaluated.

• ROI analyzed.

• Marketing performance assessed.

Recommended Actions

• Improve low-performing campaigns.

• Increase investment in campaigns with higher ROI.

Overall Marketing Health:
{"Excellent" if average_roi > 30 else "Good" if average_roi > 20 else "Needs Improvement"}
"""

    st.text_area(
        "Marketing Report",
        summary,
        height=260
    )

    report = generate_marketing_report(summary)

    st.download_button(
    label="⬇ Download Marketing Report",
    data=report,
    file_name="Marketing_Report.txt",
    mime="text/plain"
    )

    st.markdown("---")
    st.caption("Built for Microsoft Agents League Hackathon 2026")