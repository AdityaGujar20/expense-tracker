from fastapi import APIRouter

from app.models.transaction import Transaction
from app.services.transactions import create_transaction, get_transaction_summary



router = APIRouter()


@router.post("/transactions")
def add_transaction(transaction: Transaction):
    return create_transaction(transaction=transaction)


@router.get("/transactions/summary/{group}")
def sum_amount_by_group(group: str):
    return get_transaction_summary(group=group)