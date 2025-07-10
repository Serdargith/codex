from pathlib import Path

class PromptManager:
    """Load prompt templates from the prompts directory."""

    def __init__(self, base_dir: str = "prompts"):
        self.base_dir = Path(__file__).resolve().parent / base_dir

    def load(self, name: str) -> str:
        path = self.base_dir / name
        if not path.exists():
            raise FileNotFoundError(f"Prompt {name} not found")
        return path.read_text(encoding="utf-8")
