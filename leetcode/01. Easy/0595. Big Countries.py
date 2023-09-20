import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world.drop(
        labels = ["continent", "gdp"],
        axis = 1,
        inplace = True
    )

    return world[(world["area"] >= 3000000) | (world["population"] >= 25000000)]