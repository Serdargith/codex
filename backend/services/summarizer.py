from summa.summarizer import summarize

async def summarize_text(text: str, ratio: float = 0.2) -> str:
    """Return a short summary using TextRank."""
    # summa expects raw text; ratio controls summary length
    return summarize(text, ratio=ratio)
