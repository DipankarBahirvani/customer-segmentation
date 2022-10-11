from datetime import datetime, timezone

from dateutil.relativedelta import relativedelta


def test_recency_segment_recent():
    from processing.create_segements import compute_recent_segment

    three_months_ago = datetime.now(timezone.utc) - relativedelta(months=3)
    result = compute_recent_segment(three_months_ago)
    assert "91-120" == result


def test_recency_segment_2_years_ago():
    from processing.create_segements import compute_recent_segment

    three_months_ago = datetime.now(timezone.utc) - relativedelta(years=2)
    result = compute_recent_segment(three_months_ago)
    assert "180+" == result


def test_compute_segment():
    from processing.create_segements import compute_frequent_segment
    result = compute_frequent_segment(10)
    assert result == "5-13"
