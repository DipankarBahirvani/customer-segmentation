from datetime import datetime, timezone


def compute_recent_segment(last_order_ts: datetime) -> str:
    """

    last_order_ts :  Timestamp of last order

    Returns:
       str:  recent segment values

    """
    days = (datetime.now(timezone.utc).date() - last_order_ts.date()).days

    if 30 <= days <= 60:
        return "30-60"
    elif 61 <= days <= 90:
        return "61-90"
    elif 91 <= days <= 120:
        return "91-120"
    elif 121 <= days <= 180:
        return "121-180"
    else:
        return "180+"


def compute_frequent_segment(total_orders: int) -> str:
    """

    Args:
        total_orders: Total orders orders by customers

    Returns:
        str : Frequent segment values

    """
    try:
        if 0 <= total_orders <= 4:
            return "0-4"
        elif 5 <= total_orders <= 13:
            return "5-13"
        elif 14 <= total_orders <= 37:
            return "14-37"
        else:
            return "38-above"
    except ValueError:
        return "error-segment"
