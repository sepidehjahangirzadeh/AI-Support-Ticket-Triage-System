"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""


from fastapi import FastAPI
from pydantic import BaseModel

from app.triage import TriageEngine


app = FastAPI(title="Support Triaging Engine")

engine = TriageEngine()

class TicketRequest(BaseModel):
    text: str


@app.post("/triage")
async def triage(
    request: TicketRequest):

    return engine.process_ticket(request.text)