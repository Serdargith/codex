from fastapi import APIRouter
from pydantic import BaseModel
from ..services.summarizer import summarize_text

router = APIRouter()

class SummaryRequest(BaseModel):
    text: str

@router.post('/summary')
async def summarize(req: SummaryRequest):
    summary = await summarize_text(req.text)
    return {"summary": summary.strip()}
