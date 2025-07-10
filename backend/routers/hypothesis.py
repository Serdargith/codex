from fastapi import APIRouter
from pydantic import BaseModel
from ..prompt_manager import PromptManager
from ..services.ai import get_provider

router = APIRouter()
manager = PromptManager()
provider = get_provider()

class HypothesisRequest(BaseModel):
    topic: str

@router.post('/hypothesis')
async def generate_hypothesis(req: HypothesisRequest):
    prompt_template = manager.load('hypothesis_prompt.txt')
    prompt = prompt_template.format(topic=req.topic)
    text = await provider.generate(prompt)
    return {"hypotheses": text.strip()}
