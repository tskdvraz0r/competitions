import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:

    return (
        products
        .set_index("product_id")
        .stack()
        .reset_index()
        .rename(
            columns = {
                "level_1": "store", 0 : "price"
            }
        )
    )