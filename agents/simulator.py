def simulate_sales(current_sales, inventory_increase):

    predicted_sales = current_sales * (
        1 + inventory_increase / 100
    )

    improvement = predicted_sales - current_sales

    return predicted_sales, improvement