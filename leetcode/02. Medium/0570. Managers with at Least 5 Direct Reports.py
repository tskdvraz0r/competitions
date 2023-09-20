import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    df_temp: pd.DataFrame = pd.DataFrame(employee.value_counts("managerId")).reset_index()
    set_count_above_five: set = set(df_temp[df_temp["count"] >= 5]["managerId"])

    return pd.DataFrame(employee[employee["id"].isin(set_count_above_five)]["name"])