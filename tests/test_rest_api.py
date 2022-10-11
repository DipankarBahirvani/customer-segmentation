def test_frequent_segment(test_app, rest_api_input):
    response = test_app.post("/voucher_amount", json=rest_api_input)

    assert response.status_code == 200
    assert response.json() == {"voucher_amount": 2640}


def test_recency_segment(test_app, rest_api_input):
    rest_api_input["segment_name"] = "recency_segment"
    response = test_app.post("/voucher_amount", json=rest_api_input)

    assert response.status_code == 200
    assert response.json() == {"voucher_amount": 2640}
