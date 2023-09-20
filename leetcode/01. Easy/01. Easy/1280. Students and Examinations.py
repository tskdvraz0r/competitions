import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
    if len(students) == 0 or len(subjects) == 0 or len(examinations) == 0:
        return pd.DataFrame(
            columns = [
                "student_id",
                "student_name",
                "subject_name",
                "attended_exams"
            ]
        )

    students["key"] = None
    subjects["key"] = None

    temp_df: pd.DataFrame = (
        students
        .merge(
            right = subjects,
            how = "outer",
            on = "key"
        )
        .merge(
            right = (
                students.merge(
                    right = examinations,
                    how = "left",
                    on = "student_id"
                )
                .value_counts(subset = ["student_id", "student_name", "subject_name"])
                .reset_index()
            ),
            how = "left",
            on = ["student_id", "student_name", "subject_name"]
        )
        .sort_values(
            by = ["student_id", "subject_name"],
            ascending = True
        )
        .rename(
            columns = {
                "count" : "attended_exams"
            }
        )
        .fillna(value = 0)
    )

    del temp_df["key"]

    return temp_df