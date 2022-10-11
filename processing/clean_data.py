import pandas as pd

pd.options.mode.chained_assignment = None


def filter_country(df: pd.DataFrame, col: str, country_name: str) -> pd.DataFrame:
    """

    Args:
        df: Input pandas data frame
        col: Column to be formatted
        country_name: Name of the country to be filtered

    Returns:
        Filtered data frame

    """

    df = df.loc[df[col] == country_name]

    return df


def filter_nan_values(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """

    Args:
        df:  Input data frame
        col: Column from which null values will be removed

    Returns: Data frome with formatted column


    """
    df = df[df[col].notna()]

    return df


def cast_to_datetime(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """

    Args:
        df:  Input data frame
        col: Column from which null values will be removed

    Returns: Data frome with formatted column
    """

    df[col] = pd.to_datetime(df[col], format="%Y-%m-%d %H:%M:%S%z")
    return df


def cast_to_int(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """

    Args:
        df:  Input data frame
        col: Column from which null values will be removed

    Returns: Data frome with formatted column
    """

    if df[col].dtype is not float:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = filter_nan_values(df, col=col)
    df[col] = df[col].astype("int")

    return df
