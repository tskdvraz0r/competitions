import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:

    employees["total_time"] = [
        end - start

        for start, end in zip(
            employees["in_time"],
            employees["out_time"]
        )
    ]

    return (
        employees
        .groupby(
            by = [
                "event_day",
                "emp_id"
            ]
        )
        .aggregate(
            {
                "total_time" : "sum"
            }
        )
        .reset_index()
        .rename(
            columns = {
                "event_day" : "day"
            }
        )
    )