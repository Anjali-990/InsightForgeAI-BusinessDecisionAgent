def generate_summary(total_sales):

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

    return summary