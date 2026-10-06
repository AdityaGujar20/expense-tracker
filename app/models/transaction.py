from pydantic import BaseModel


class Transaction(BaseModel):
    date: str
    amount: float
    group: str
