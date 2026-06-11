import pandas as pd

def detect_anomalies(df):

    insights = []

    regions = df["Region"].unique()

    for region in regions:

        region_data = df[df["Region"] == region]

        first_sales = region_data["Sales"].iloc[0]
        last_sales = region_data["Sales"].iloc[-1]

        sales_change = ((last_sales - first_sales) / first_sales) * 100

        if sales_change < -10:
            insights.append(
                f"Sales dropped {abs(sales_change):.1f}% in {region} Region."
            )

        first_inventory = region_data["Inventory"].iloc[0]
        last_inventory = region_data["Inventory"].iloc[-1]

        inventory_change = ((last_inventory - first_inventory) / first_inventory) * 100

        if inventory_change < -10:
            insights.append(
                f"Inventory decreased {abs(inventory_change):.1f}% in {region} Region."
            )

        first_customers = region_data["Customers"].iloc[0]
        last_customers = region_data["Customers"].iloc[-1]

        customer_change = ((last_customers - first_customers) / first_customers) * 100

        if customer_change < -10:
            insights.append(
                f"Customer count decreased {abs(customer_change):.1f}% in {region} Region."
            )

    return insights