def generate_recommendations(df):

    recommendations = []

    regions = df["Region"].unique()

    for region in regions:

        region_data = df[df["Region"] == region]

        sales_start = region_data["Sales"].iloc[0]
        sales_end = region_data["Sales"].iloc[-1]

        inventory_start = region_data["Inventory"].iloc[0]
        inventory_end = region_data["Inventory"].iloc[-1]

        customers_start = region_data["Customers"].iloc[0]
        customers_end = region_data["Customers"].iloc[-1]

        if inventory_end < inventory_start:
            recommendations.append(
                f"Increase inventory levels in {region} Region to prevent stock shortages."
            )

        if customers_end < customers_start:
            recommendations.append(
                f"Launch a customer retention campaign in {region} Region."
            )

        if sales_end < sales_start:
            recommendations.append(
                f"Monitor sales trends weekly and investigate declining demand in {region} Region."
            )

    return recommendations