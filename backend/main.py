from fastapi import FastAPI
from .routers import hypothesis

app = FastAPI(title="Article Assistant")

app.include_router(hypothesis.router)

@app.get('/')
async def root():
    return {"message": "Article Assistant API"}
