def detect_dataset(df):
    columns = [col.lower() for col in df.columns]

    sales_keywords = [
        "sales",
        "inventory",
        "customers",
        "region"
    ]

    hr_keywords = [
        "employee",
        "department",
        "salary",
        "experience"
    ]

    finance_keywords = [
        "revenue",
        "expense",
        "profit",
        "cost"
    ]

    marketing_keywords = [
        "campaign",
        "clicks",
        "ctr",
        "impressions",
        "roi"
    ]

    if any(col in columns for col in sales_keywords):
        return "sales"

    elif any(col in columns for col in hr_keywords):
        return "hr"

    elif any(col in columns for col in finance_keywords):
        return "finance"

    elif any(col in columns for col in marketing_keywords):
        return "marketing"

    return "unknown"