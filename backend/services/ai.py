from typing import Optional
import os

try:
    from transformers import pipeline
except ImportError:  # transformers not installed
    pipeline = None

class AIProvider:
    """Base class for text generation providers."""

    async def generate(self, prompt: str) -> str:
        raise NotImplementedError


class HuggingFaceProvider(AIProvider):
    """Generate text using a local HuggingFace model."""

    def __init__(self, model_path: Optional[str] = None):
        if pipeline is None:
            raise RuntimeError("transformers must be installed to use HuggingFaceProvider")
        self.model_path = model_path or os.environ.get("HF_MODEL_PATH", "gpt2")
        self.generator = pipeline("text-generation", model=self.model_path)

    async def generate(self, prompt: str) -> str:
        outputs = self.generator(prompt, max_length=512, num_return_sequences=1)
        return outputs[0]["generated_text"]


def get_provider() -> AIProvider:
    """Return the configured AI provider. Defaults to HuggingFaceProvider."""

    return HuggingFaceProvider()
