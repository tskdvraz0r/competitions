import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    low_salary = 0
    average_salary = 0
    high_salary = 0

    for income in accounts['income']:
        if income < 20000:
            low_salary += 1
        
        elif 20000 <= income <= 50000:
            average_salary += 1
        
        else:
            high_salary += 1
        
    return (
        pd.DataFrame(
            data = zip(
                [
                    "Low Salary",
                    "Average Salary",
                    "High Salary"
                ],
                [
                    low_salary,
                    average_salary,
                    high_salary
                ]
            ),
            columns = [
                "category",
                "accounts_count"
            ]
        )
        .sort_values(
            by = "accounts_count",
            ascending = False
        )
    )