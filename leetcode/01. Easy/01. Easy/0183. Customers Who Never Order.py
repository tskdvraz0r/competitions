import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    df_result: pd.DataFrame = (
        customers
        .rename(
            columns = {
                "id" : "customerId",
                "name" : "Customers"
            }
        )
        .merge(
            right = orders,
            how = "left",
            on = "customerId"
        )
    )

    return df_result[df_result["id"].isna()].drop(labels = ["customerId", "id"], axis = 1)