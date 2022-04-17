import pandas as pd

def project(df: pd.DataFrame):
    return df[["state", "votes"]]


def group_count(df: pd.DataFrame):
    return df.groupby("party").count()


def sort(df: pd.DataFrame):
    return df.sort_values("votes", ascending=False)


def flip_bool(df: pd.DataFrame):
    return df["won"].apply(lambda _bool: not _bool)


def find_max(df: pd.DataFrame):
    return df["votes"].max()


def select(df: pd.DataFrame):
    return df[(df["party"] == "DEM") & (df["won"]) & (df["votes"] > 20000)]


def select_group_mean(df: pd.DataFrame):
    return df[df["won"]].groupby("party").mean()


def longest_string_in_column(df: pd.DataFrame):
    return df["candidate"].apply(lambda name: len(name)).max()


def join(df: pd.DataFrame):
    return pd.merge(df, df, how="inner", on="unique_col")


def select_p90_cols(df: pd.DataFrame):
    return df.iloc[:, 1: round(df.shape[1] * 0.9)]


def select_p90_rows(df: pd.DataFrame):
    return df.iloc[1: round(df.shape[0] * 0.9)]


def combine_cols(df: pd.DataFrame):
    df["combined"] = df["candidate"] + " " + df["party"] + " " + df["won"].astype(str)
    return df
