from fastapi import FastAPI
app = FastAPI()

orders = {}

@app.post("/create_order")
def create_order():
    order_id = len(orders) + 1
    orders[order_id] = "PENDING"
    return {"id": order_id}

@app.post("/cancel_order")
def cancel_order(order_id: int):
    orders[order_id] = "CANCELLED"
    return {"status": "cancelled"}
