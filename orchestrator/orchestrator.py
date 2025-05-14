import requests

def orchestrate(order_id: int):
    print(f"\n➡️ Starting saga for Order ID: {order_id}")

    # Create order
    try:
        res = requests.post("http://localhost:8001/create_order")
        print(f"🛒 Order created: {res.json()}")
        res.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to create order: {e}")
        return

    # Payment step
    try:
        res = requests.post("http://localhost:8002/pay", json={"order_id": order_id})
        print(f"💳 Payment response: {res.status_code} {res.text}")
        res.raise_for_status()
    except Exception as e:
        print(f"❌ Payment failed: {e}")
        print("🔁 Cancelling order...")
        requests.post("http://localhost:8001/cancel_order", params={"order_id": order_id})
        return

    # Inventory step
    try:
        res = requests.post("http://localhost:8003/reserve", json={"order_id": order_id})
        print(f"📦 Inventory response: {res.status_code} {res.text}")
        res.raise_for_status()
    except Exception as e:
        print(f"❌ Inventory failed: {e}")
        print("🔁 Refunding and cancelling order...")
        requests.post("http://localhost:8002/refund", json={"order_id": order_id})
        requests.post("http://localhost:8001/cancel_order", params={"order_id": order_id})
        return

    print("✅ Saga completed successfully 🎉")

if __name__ == "__main__":
    orchestrate(order_id=1)  # Change to 2 to simulate failure
