"""
Ollama LLM configuration: Llama 3, DeepSeek, or any Ollama model.
Uses LLAMA_API_TOKEN and LLAMA_API_BASE — no OPENAI_API_KEY.
"""
import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

# Model: any Ollama model, e.g. ollama/llama3:8b or ollama/deepseek-r1
LLAMA_MODEL = os.getenv("LLAMA_MODEL", "ollama/llama3:8b")


def get_llama_llm() -> LLM:
    """Build CrewAI LLM for Ollama (Llama 3, DeepSeek, etc.) using LLAMA_API_TOKEN and LLAMA_API_BASE."""
    token = os.getenv("LLAMA_API_TOKEN", "")
    base_url = os.getenv("LLAMA_API_BASE", "http://localhost:11434").strip().rstrip("/")
    # Ollama OpenAI-compatible endpoint is /v1/chat/completions; use base without /v1 so client adds it
    if base_url.endswith("/v1"):
        base_url = base_url[:-3].rstrip("/")

    # Use token if set; otherwise "ollama" so CrewAI doesn't fall back to OPENAI_API_KEY
    api_key = token if token else "ollama"

    return LLM(
        model=LLAMA_MODEL,
        base_url=base_url,
        api_key=api_key,
        temperature=0.7,
    )


llm = get_llama_llm()
