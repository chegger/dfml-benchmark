import polars as pl

def project(df: pl.DataFrame):
    return df.lazy().select(["state", "votes"]).collect()


def group_count(df: pl.DataFrame):
    return df.lazy().groupby("party").agg(pl.count("unique_col")).collect()


def sort(df: pl.DataFrame):
    return df.lazy().sort(by="votes", reverse=True).collect()


def flip_bool(df: pl.DataFrame):
    return df.lazy().select([pl.col("won").is_not()]).collect()


def find_max(df: pl.DataFrame):
    return df.lazy().select("votes").max().collect()


def select(df: pl.DataFrame):
    return df.lazy().filter((pl.col("party") == "DEM") & (pl.col("votes") > 20000) & pl.col("won")).collect()


def select_group_mean(df: pl.DataFrame):
    return df.lazy().filter(pl.col("won")).groupby("party").agg(pl.col("votes").mean()).collect()


def longest_string_in_column(df: pl.DataFrame):
    return df.lazy().select([pl.col("candidate").apply(len).max()]).collect()


def join(df: pl.DataFrame):
    return df.lazy().join(df.lazy(), on="unique_col", how="inner").collect()


def select_p90_cols(df: pl.DataFrame):
    return df[:, 1: round(df.shape[1] * 0.9)]


def select_p90_rows(df: pl.DataFrame):
    return df[1: round(df.shape[0] * 0.9)]


def combine_cols(df: pl.DataFrame):
    return df\
        .lazy()\
        .with_columns([pl
                      .concat_str(["candidate", "party", "won"], sep=" ")
                      .alias("combined")]).collect()
