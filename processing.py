import json

from typer import Typer,Option
import pandas as pd
import logging

logger = logging.getLogger(__name__)

app = Typer()


@app.command()
def clean_data(source_file_path:str=Option(
        ...,
        help="Input path of the raw parquet file",
    ),)->pd.DataFrame:
    from processing.clean_data import (
        filter_country,
        cast_to_datetime,
        cast_to_int,
    )
    logger.info(f"Reading parquet file")
    df = pd.read_parquet(source_file_path)

    integer_cols = ["voucher_amount", "total_orders"]
    for col_name in integer_cols:
        df = cast_to_int(df, col=col_name)

    timestamp_cols = ["timestamp", "last_order_ts", "first_order_ts"]

    for col_name in timestamp_cols:
        df = cast_to_datetime(df, col=col_name)

    df = filter_country(df, country_name="Peru", col="country_code")

    logger.info(f"Numer of records are {df.count()}")

    return df


@app.command()
def clean_and_process_data(source_file_path: str=Option(
        ...,
        help="Input path of the raw parquet file",
    )):
    df = clean_data(source_file_path)

    from processing.create_segements import (
        compute_recent_segment,
        compute_frequent_segment,
    )

    df["frequent_segment"] = df["total_orders"].apply(compute_frequent_segment)
    df["recent_segment"] = df["last_order_ts"].apply(compute_recent_segment)

    df_frequency_segment = df.groupby("frequent_segment", as_index=True).agg(
        {"voucher_amount": lambda x: x.value_counts().index[0]}
    )
    df_recent_segment = df.groupby("recent_segment", as_index=True).agg(
        {"voucher_amount": lambda x: x.value_counts().index[0]}
    )

    ## In production write these df to a key-value store. For now dump it as json and use later
    recent_segment = df_recent_segment.to_dict()["voucher_amount"]
    frequent_segment = df_frequency_segment.to_dict()["voucher_amount"]
    logger.info("Writing segment files")
    with open("data/enriched/recent_segment.json", "w") as fp:
        json.dump(recent_segment, fp, indent=4)

    with open("data/enriched/frequent_segment.json", "w") as fp:
        json.dump(frequent_segment, fp, indent=4)
    logger.info("Segments data files are written to data/enriched")


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    app()
