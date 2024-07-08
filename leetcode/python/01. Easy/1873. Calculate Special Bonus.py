import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    employees["bonus"] = [
        salary if (name[0] != "M") and (id % 2 != 0) else 0

        for name, salary, id in zip(
            employees["name"],
            employees["salary"],
            employees["employee_id"]
        )
    ]

    return employees[["employee_id", "bonus"]].sort_values(
        by = "employee_id",
        ascending = True
    )