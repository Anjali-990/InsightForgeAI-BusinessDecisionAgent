import streamlit as st
import matplotlib.pyplot as plt

from agents.report_generator import generate_hr_report
def show_hr_dashboard(df):

    st.header("👥 HR Analysis")
    st.write("## Human Resources Overview")

    # ==========================
    # KPIs
    # ==========================

    total_employees = len(df)
    average_salary = df["Salary"].mean()
    average_experience = df["Experience"].mean()
    departments = df["Department"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👥 Employees",
            total_employees
        )

    with col2:
        st.metric(
            "💰 Avg Salary",
            f"{average_salary:,.0f}"
        )

    with col3:
        st.metric(
            "📅 Avg Experience",
            f"{average_experience:.1f} Years"
        )

    with col4:
        st.metric(
            "🏢 Departments",
            departments
        )

    st.success("HR analysis completed!")

    # ==========================
    # Department Distribution
    # ==========================

    st.header("🏢 Employees by Department")

    dept = df["Department"].value_counts()

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        dept.index,
        dept.values
    )

    ax.set_xlabel("Department")
    ax.set_ylabel("Employees")
    ax.set_title("Department Distribution")

    st.pyplot(fig)

    # ==========================
    # Salary Distribution
    # ==========================

    st.header("💰 Salary Distribution")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.hist(df["Salary"], bins=5)

    ax.set_xlabel("Salary")
    ax.set_ylabel("Employees")
    ax.set_title("Salary Distribution")

    st.pyplot(fig)

    # ==========================
    # Experience Distribution
    # ==========================

    st.header("📅 Experience Distribution")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        df["Employee"],
        df["Experience"]
    )

    ax.set_xlabel("Employee")
    ax.set_ylabel("Years")
    ax.set_title("Employee Experience")

    plt.xticks(rotation=45)

    st.pyplot(fig)

    # ==========================
    # Workforce Health
    # ==========================

    st.header("📈 Workforce Health")

    col1, col2 = st.columns(2)

    experienced = len(df[df["Experience"] >= 5])
    experienced_percent = (experienced / total_employees) * 100

    high_salary = len(df[df["Salary"] > average_salary])
    salary_percent = (high_salary / total_employees) * 100

    with col1:
        st.metric(
            "Experienced Employees",
            f"{experienced_percent:.1f}%"
        )

    with col2:
        st.metric(
            "Above Avg Salary",
            f"{salary_percent:.1f}%"
        )

    # ==========================
    # HR Risk Assessment
    # ==========================

    st.header("🚨 HR Risk Assessment")

    risks = []

    if average_experience < 3:
        risks.append(
            "⚠️ Workforce experience is relatively low."
        )

    if departments < 3:
        risks.append(
            "⚠️ Limited departmental diversity."
        )

    if average_salary < 30000:
        risks.append(
            "⚠️ Salary levels may affect employee retention."
        )

    if risks:
        for risk in risks:
            st.warning(risk)
    else:
        st.success("No major HR risks detected.")

    # ==========================
    # HR Reasoning
    # ==========================

    st.header("🧠 HR Reasoning")

    reasons = []

    if average_experience < 3:
        reasons.append(
            "Lower average experience may reduce overall productivity."
        )

    if average_salary < 30000:
        reasons.append(
            "Lower salaries could contribute to higher employee turnover."
        )

    if average_experience >= 5:
        reasons.append(
            "Experienced workforce provides operational stability."
        )

    if reasons:
        for reason in reasons:
            st.info(reason)
    else:
        st.success("HR indicators appear stable.")

    # ==========================
    # Recommendations
    # ==========================

    st.header("✅ Recommendations")

    recommendations = []

    if average_salary < 30000:
        recommendations.append(
            "Review compensation policies."
        )

    if average_experience < 3:
        recommendations.append(
            "Increase employee training programs."
        )

    if departments < 3:
        recommendations.append(
            "Expand organizational capabilities."
        )

    if not recommendations:
        recommendations.append(
            "Maintain current HR strategy."
        )

    for rec in recommendations:
        st.success(rec)

    # ==========================
    # Executive Summary
    # ==========================

    st.header("📋 Executive Summary")

    summary = f"""
HR Performance Summary

Total Employees: {total_employees}

Average Salary: {average_salary:,.0f}

Average Experience: {average_experience:.1f} Years

Departments: {departments}

Key Findings

• Workforce analyzed successfully.

• Employee distribution evaluated.

• HR risks assessed.

Recommended Actions

• Continue investing in employee development.

• Review compensation annually.

• Monitor workforce growth and retention.

Overall HR Health: Stable
"""

    st.text_area(
        "HR Report",
        summary,
        height=260
    )

    
    report = generate_hr_report(summary)

    st.download_button(
    label="⬇ Download HR Report",
    data=report,
    file_name="HR_Report.txt",
    mime="text/plain"
    )
    st.markdown("---")
    st.caption("Built for Microsoft Agents League Hackathon 2026")