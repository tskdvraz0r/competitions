import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    delivery["time"] = [
        1 if order == deliver else 0

        for order, deliver in zip(
            delivery["order_date"],
            delivery["customer_pref_delivery_date"]
        )
    ]

    immediate_count = list(delivery["time"]).count(1)
    total = len(delivery)

    return pd.DataFrame(zip([round(immediate_count / total * 100, 2)]), columns = ["immediate_percentage"])