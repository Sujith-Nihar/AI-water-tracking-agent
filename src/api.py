from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake_history
from src.logger import log_message


app = FastAPI()
agent = WaterIntakeAgent()

class WaterIntakeRequest(BaseModel):
    UserId: str
    Intake: int

@app.post("/log-intake")
async def log_water_intake(request: WaterIntakeRequest):
    log_intake(request.UserId, request.Intake)
    analysis = agent.analyze_intake(request.Intake)
    log_message(f"user {request.UserId} logged {request.Intake} ml")
    return {"message": "Water intake logged successfully", "analysis": analysis}

@app.get("/history/{UserId}")
async def get_water_history(UserId: str):
    history = get_intake_history(UserId)
    return {"UserId": UserId, "history": history}