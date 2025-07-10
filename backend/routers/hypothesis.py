from fastapi import APIRouter
from pydantic import BaseModel
from openai import ChatCompletion

from ..prompt_manager import PromptManager

router = APIRouter()
manager = PromptManager()

class HypothesisRequest(BaseModel):
    topic: str

@router.post('/hypothesis')
async def generate_hypothesis(req: HypothesisRequest):
    prompt_template = manager.load('hypothesis_prompt.txt')
    prompt = prompt_template.format(topic=req.topic)
    response = ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    text = response.choices[0].message['content']
    return {"hypotheses": text.strip()}
