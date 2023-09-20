import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    views.drop(labels = ["view_date", "article_id"], axis = 1, inplace = True)
    views.drop_duplicates(inplace = True)

    return (
        views[views["author_id"] == views["viewer_id"]]
        .drop(
            labels = "viewer_id",
            axis = 1
        )
        .rename(
            columns = {
                "author_id" : "id"
            }
        )
        .sort_values(
            by = "id",
            ascending = True
        )
    )