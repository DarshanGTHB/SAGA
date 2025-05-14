from fastapi import FastAPI, Request
app = FastAPI()

@app.post("/reserve")
async def reserve(request: Request):
    return {"status": "reserved"}
