def generate_reasoning(df):

    reasons = []

    regions = df["Region"].unique()

    for region in regions:

        region_data = df[df["Region"] == region]

        sales_start = region_data["Sales"].iloc[0]
        sales_end = region_data["Sales"].iloc[-1]

        inventory_start = region_data["Inventory"].iloc[0]
        inventory_end = region_data["Inventory"].iloc[-1]

        customers_start = region_data["Customers"].iloc[0]
        customers_end = region_data["Customers"].iloc[-1]

        sales_drop = sales_end < sales_start
        inventory_drop = inventory_end < inventory_start
        customer_drop = customers_end < customers_start

        if sales_drop and inventory_drop:
            reasons.append(
                f"In {region} Region, sales decline appears strongly correlated with inventory shortages."
            )

        if sales_drop and customer_drop:
            reasons.append(
                f"In {region} Region, declining customer numbers likely contributed to lower revenue."
            )

    return reasons