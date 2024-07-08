import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    if len(list(set(employee["salary"]))) < N:
        
        return pd.DataFrame(
            data = [None],
            columns = ["SecondHighestSalary"]
        )

    elif len(list(set(employee["salary"]))) == 1:
        
        return pd.DataFrame(
            data = [sorted(list(set(employee["salary"])))[0]],
            columns = ["SecondHighestSalary"]
        )
            
    else:

        return pd.DataFrame(
            data = [sorted(list(set(employee["salary"])))[-N]],
            columns = ["SecondHighestSalary"]
        )