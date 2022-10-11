import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException  # pylint: disable=import-error
from pydantic import BaseModel

from processing.create_segements import compute_frequent_segment, compute_recent_segment

cwd = Path(__file__).parent.resolve()
rel_freq_path = "../data/enriched/frequent_segment.json"
rel_rec_path = "../data/enriched/recent_segment.json"

# For poc purpose. In prod, we should use a key-value store eg Dynamodb
with open((cwd / rel_freq_path), "r") as j:
    frequent_lookup = json.loads(j.read())

# For poc purpose. In prod, we should use a key-value store eg Dynamodb


with open((cwd / rel_rec_path), "r") as j:
    recent_lookup = json.loads(j.read())


class Customer(BaseModel):
    customer_id: int
    country_code: Literal["Peru"]
    first_order_ts: datetime
    last_order_ts: datetime
    total_order: int
    segment_name: str


class Voucher(BaseModel):
    voucher_amount: int


app = FastAPI()


# @app.get("/")
# def root():
#     return {"message:Welcome"}


@app.post("/voucher_amount", response_model=Voucher)
def get_voucher_amount(customer: Customer) -> dict:
    """

    Args:
        customer: request body from the client

    Returns:
        voucher_amount: Dict of voucher_amount and the value

    """
    if customer.segment_name not in ["recency_segment", "frequent_segment"]:
        raise HTTPException(
            status_code=404,
            detail="Invalid Segment Name. The segment name is should be recency_segment or frequent_segment",
        )

    elif customer.segment_name == "recency_segment":
        segment = compute_recent_segment(last_order_ts=customer.last_order_ts)
        if segment in recent_lookup:
            return {"voucher_amount": recent_lookup[segment]}
        else:
            raise HTTPException(
                status_code=404, detail="Recency_segment not found in the DB"
            )

    else:
        segment = compute_frequent_segment(total_orders=customer.total_order)
        print(segment)
        print(frequent_lookup)
        if segment in frequent_lookup:
            return {"voucher_amount": frequent_lookup[segment]}

        else:
            raise HTTPException(
                status_code=404, detail="Recency_segment not found in the DB"
            )
