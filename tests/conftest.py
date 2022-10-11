import numpy as np
import pandas as pd
import pytest
from starlette.testclient import TestClient  # pylint: disable=import-error

from api.main import app


@pytest.fixture
def input_value(scope="module"):
    data = {
        "country": ["Germany", "Peru", "India"],
        "total_order": ["123.0", "14.0", np.nan],
        "order_ts": [
            "2022-01-04 00:00:00+00:00",
            "2022-01-04 00:00:00+00:00",
            "2022-01-04 00:00:00+00:00",
        ],
    }

    df = pd.DataFrame(data)

    return df


@pytest.fixture(scope="module")
def rest_api_input():
    body = {
        "customer_id": 1,
        "country_code": "Peru",
        "first_order_ts": "2022-01-04 00:00:00",
        "last_order_ts": "2022-01-04 00:00:00",
        "total_order": 100,
        "segment_name": "frequent_segment",
    }
    return body


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here
