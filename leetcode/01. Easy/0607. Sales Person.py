import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    df_merge = (
        sales_person[["sales_id", "name"]]
        .merge(
            right = orders[["sales_id", "com_id"]],
            how = "left",
            on = "sales_id"
        )
        .merge(
            right = (
                company[["com_id", "name"]]
                .rename(
                    columns = {
                        "name" : "company_name"
                    }
                )
            ),
            how = "left",
            on = "com_id"
        )
    )
    
    red_sales = set(df_merge[df_merge["company_name"] == "RED"]["name"])

    return pd.DataFrame(df_merge[~df_merge["name"].isin(red_sales)]["name"]).drop_duplicates(subset = "name")