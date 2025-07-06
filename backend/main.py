from fastapi import FastAPI, Request
from backend.ultimate_apple_purchase import UltimateApplePurchaseSystem
from backend.memory.vector_memory import log_result

app = FastAPI()

@app.post("/api/run_purchase")
async def run_purchase(request: Request):
    task = await request.json()
    system = UltimateApplePurchaseSystem(task)
    result = system.execute()
    log_result(task, result)
    return result
