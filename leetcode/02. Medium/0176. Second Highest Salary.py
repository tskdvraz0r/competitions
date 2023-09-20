import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    if len(list(set(employee["salary"]))) <= 1:
        
        return pd.DataFrame(
            data = [None],
            columns = ["SecondHighestSalary"]
        )
    
    else:

        return pd.DataFrame(
            data = [sorted(list(set(employee["salary"])))[-2]],
            columns = ["SecondHighestSalary"]
        )