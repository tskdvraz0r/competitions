import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals.sort_values(by="weight", ascending=False, inplace=True)

    return pd.DataFrame(animals[animals["weight"] > 100]["name"])