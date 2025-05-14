from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse  # Import JSONResponse

app = FastAPI()

@app.post("/pay")
async def pay(request: Request):
    body = await request.json()
    order_id = body["order_id"]
    if order_id % 2 == 0:  # Simulate failure
        return JSONResponse(content={"status": "fail"}, status_code=500)  # Correct way to return status code and body
    return {"status": "paid"}

@app.post("/refund")
async def refund(request: Request):
    return {"status": "refunded"}
