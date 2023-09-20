import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    tweets["len"] = [len(content) for content in tweets["content"]]

    return (
        tweets[tweets["len"] > 15]
        .drop(
            labels = [
                "content",
                "len"
            ],
            axis = 1
        )
    )