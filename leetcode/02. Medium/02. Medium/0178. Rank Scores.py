import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    scores.drop(
        labels = "id",
        axis = 1,
        inplace = True
    )

    scores["rank"] = scores.rank(method = "dense", ascending = False)

    return scores.sort_values("score", ascending = False)