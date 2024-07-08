import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    
    activities = pd.DataFrame(activities.groupby("sell_date")["product"].apply(set)).reset_index().rename(columns = {"product" : "products"})
    activities['products'] = activities['products'].apply(lambda x: sorted(list(x)))
    activities["num_sold"] = [len(product) for product in activities["products"]]
    activities['products'] = activities['products'].apply(','.join)

    return activities[["sell_date", "num_sold", "products"]]