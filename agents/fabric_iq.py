def generate_fabric_iq(df):

    entities = []

    relationships = []

    risk = "Low"

    # Detect entities
    for column in df.columns:
        entities.append(column)

    # Check each region
    if "Region" in df.columns:

        regions = df["Region"].unique()

        for region in regions:

            region_df = df[df["Region"] == region]

            sales_start = region_df["Sales"].iloc[0]
            sales_end = region_df["Sales"].iloc[-1]

            inventory_start = region_df["Inventory"].iloc[0]
            inventory_end = region_df["Inventory"].iloc[-1]

            customers_start = region_df["Customers"].iloc[0]
            customers_end = region_df["Customers"].iloc[-1]

            sales_change = (
                (sales_end - sales_start)
                / sales_start
            ) * 100

            inventory_change = (
                (inventory_end - inventory_start)
                / inventory_start
            ) * 100

            customer_change = (
                (customers_end - customers_start)
                / customers_start
            ) * 100

            if sales_change < -10 and inventory_change < -10:

                relationships.append(
                    f"{region}: Inventory ↓ {abs(inventory_change):.1f}% → Sales ↓ {abs(sales_change):.1f}%"
                )

            if sales_change < -10 and customer_change < -10:

                relationships.append(
                    f"{region}: Customers ↓ {abs(customer_change):.1f}% → Sales ↓ {abs(sales_change):.1f}%"
                )

            if sales_change < -20:

                risk = "High"

            elif sales_change < -10:

                risk = "Medium"

    return entities, relationships, risk