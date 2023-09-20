import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:

    return (
        actor_director
        .value_counts(["actor_id", "director_id"])
        .reset_index()
        .query("count >= 3")
        .drop(labels = "count", axis = 1)
    )