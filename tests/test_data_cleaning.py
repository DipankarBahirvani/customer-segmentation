def test_filter_nan_values(input_value):
    from processing.clean_data import filter_nan_values

    df = filter_nan_values(input_value, col="total_order")
    assert df["total_order"].isnull().sum() == 0


def test_country_filter(input_value):
    from processing.clean_data import filter_country

    df = filter_country(input_value, country_name="Peru", col="country")
    assert df["country"].count() == 1


def test_cast_to_int(input_value):
    from processing.clean_data import cast_to_int

    df = cast_to_int(input_value, col="total_order")
    assert df.total_order.dtype == "int"


def test_cast_to_datetime(input_value):
    from processing.clean_data import cast_to_datetime

    df = cast_to_datetime(input_value, col="order_ts")
    val = "datetime" in str(df.order_ts.dtype)
    assert val == True
