import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:

    temp_df = (
        orders
        .groupby("customer_number")
        .aggregate(
            {
                "order_number" : "count"
            }
        )
        .reset_index()
        .sort_values(
            by = "order_number",
            ascending = False
        )
    )

    return (
        temp_df[temp_df["order_number"] == temp_df["order_number"].max()]
        .drop(
            labels = "order_number",
            axis = 1
        )
    )