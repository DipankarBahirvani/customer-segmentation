import requests

url = 'http://127.0.0.1:80/voucher_amount'
data = {
        "customer_id": 1,
        "country_code": "Peru",
        "first_order_ts": "2018-01-04 00:00:00",
        "last_order_ts": "2021-01-04 00:00:00",
        "total_order": 100,
        "segment_name": "recency_segment",
}

response = requests.post(url, json=data)

print(response.text)

data["segment_name"] = "frequent_segment"

response = requests.post(url, json=data)

print(response.text)
