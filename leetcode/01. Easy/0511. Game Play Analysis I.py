import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    return (
        activity
        .sort_values(
            by = "event_date",
            ascending = True
        )
        .drop_duplicates(
            subset = "player_id"
        )
        .drop(
            labels = [
                "device_id",
                "games_played"
            ],
            axis = 1
        )
        .rename(
            columns = {
                "event_date" : "first_login"
            }
        )
    )