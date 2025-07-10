from fastapi import FastAPI
from .routers import hypothesis, summary

app = FastAPI(title="Article Assistant")

app.include_router(hypothesis.router)
app.include_router(summary.router)

@app.get('/')
async def root():
    return {"message": "Article Assistant API"}
