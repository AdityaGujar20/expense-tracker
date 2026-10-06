from pymongo import MongoClient

from app.models.transaction import Transaction

# URL = "mongodb://admin:password@localhost:27017/"
URL = "mongodb://admin:password@mongodb:27017/?authSource=admin"


def create_transaction(transaction: Transaction):
    client = MongoClient(URL)

    db = client["finance"]
    transactions = db["transactions"]

    transactions.insert_one(transaction.model_dump())
    client.close()

    return "transaction added"


def get_transaction_summary(group: str):
    client = MongoClient(URL)

    db = client["finance"]
    transactions = db["transactions"]

    result = transactions.aggregate([
        {
            "$match": {
                "group": group
            }
        },
        {
            "$group": {
                "_id": "$group",
                "total": {
                    "$sum": "$amount"
                }
            }
        }
    ])

    client.close()

    return list(result)


if __name__ == "__main__":
    transaction1 = Transaction(date="2026-10-04", amount=40, group="cold drink")
    create_transaction(transaction=transaction1)

