import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = [
        name if name[0] in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0] else name.title()
        for name in users["name"]
    ]

    return users.sort_values(by = "user_id", ascending = True)