import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    employee = (
        employee
        .merge(
            right = (
                department
                .rename(
                    columns = {
                        "id" : "departmentId",
                        "name" : "Department"
                    }
                )
            ),
            how = "inner",
            on = "departmentId"
        )
    )

    temp_df = (
        employee
        .groupby(
            by = [
                "Department",
                "departmentId"
            ]
        )
        .aggregate(
            {
                "salary" : "max"
            }
        )
        .reset_index()
        .merge(
            right = employee[
                [
                    "name",
                    "salary",
                    "departmentId"
                ]
            ],
            how = "inner",
            on = [
                "departmentId",
                "salary"
            ]
        )
        .rename(
            columns = {
                "name" : "Employee",
                "salary" : "Salary"
            }
        )
    )

    return temp_df[
        [
            "Department",
            "Employee",
            "Salary"
        ]
    ]