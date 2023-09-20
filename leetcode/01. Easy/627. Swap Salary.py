import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary["sex"] = [
        x.replace("m", "f") if x == "m" else x.replace("f", "m")

        for x in salary["sex"]
    ]

    return salary