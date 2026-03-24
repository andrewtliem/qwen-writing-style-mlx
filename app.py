from __future__ import annotations

import os
import subprocess
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# =============================
# Configuration
# =============================
BASE_MODEL = os.getenv("MLX_BASE_MODEL", "mlx-community/Qwen2.5-0.5B-Instruct-4bit")
# This should point to a local adapter directory on the current machine.
ADAPTER_PATH = os.getenv(
    "MLX_ADAPTER_PATH",
    "./qwen25_v9",
)
MLX_BIN = os.getenv("MLX_BIN", "mlx_lm.generate")

DEFAULT_INSTRUCTION = (
    "Rewrite the following in a formal EPON research paper style. "
)

MAX_INPUT_CHARS = int(os.getenv("MAX_INPUT_CHARS", "4000"))
DEFAULT_MAX_TOKENS = int(os.getenv("DEFAULT_MAX_TOKENS", "220"))
DEFAULT_TEMP = float(os.getenv("DEFAULT_TEMP", "0.3"))
DEFAULT_TOP_P = float(os.getenv("DEFAULT_TOP_P", "0.9"))

# =============================
# App Init
# =============================
app = FastAPI(title="Qwen LoRA Fine-Tune Tutorial API", version="1.0.0")

# =============================
# CORS (IMPORTANT FIX)
# =============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================
# Request / Response Models
# =============================
class RewriteRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=MAX_INPUT_CHARS)
    instruction: Optional[str] = DEFAULT_INSTRUCTION
    max_tokens: int = Field(default=DEFAULT_MAX_TOKENS, ge=32, le=512)
    temperature: float = Field(default=DEFAULT_TEMP, ge=0.0, le=1.5)
    top_p: float = Field(default=DEFAULT_TOP_P, ge=0.1, le=1.0)


class RewriteResponse(BaseModel):
    rewritten_text: str
    raw_output: str


# =============================
# Helper Functions
# =============================
def extract_generation(stdout: str) -> str:
    parts = stdout.split("==========")
    if len(parts) >= 3:
        return parts[1].strip()
    return stdout.strip()


def run_mlx(prompt: str, max_tokens: int, temp: float, top_p: float) -> str:
    cmd = [
        MLX_BIN,
        "--model", BASE_MODEL,
        "--adapter-path", ADAPTER_PATH,
        "--prompt", prompt,
        "--max-tokens", str(max_tokens),
        "--temp", str(temp),
        "--top-p", str(top_p),
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120,
        )
    except FileNotFoundError:
        raise HTTPException(
            status_code=500,
            detail="mlx_lm.generate not found. Activate your environment.",
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="Model timeout")

    if result.returncode != 0:
        raise HTTPException(status_code=500, detail=result.stderr)

    return result.stdout


# =============================
# Routes
# =============================
@app.get("/health")
def health():
    return {
        "status": "ok",
        "model": BASE_MODEL,
        "adapter": ADAPTER_PATH,
    }


@app.post("/rewrite", response_model=RewriteResponse)
def rewrite(req: RewriteRequest):
    if len(req.text) > MAX_INPUT_CHARS:
        raise HTTPException(status_code=400, detail="Input too long")

    prompt = f"{req.instruction}\n\n{req.text}"

    output = run_mlx(
        prompt=prompt,
        max_tokens=req.max_tokens,
        temp=req.temperature,
        top_p=req.top_p,
    )

    cleaned = extract_generation(output)

    return RewriteResponse(
        rewritten_text=cleaned,
        raw_output=output,
    )


@app.get("/")
def root():
    return {
        "message": "Qwen LoRA Fine-Tune Tutorial API is running",
        "tutorial": "Local FastAPI wrapper for a Qwen LoRA adapter",
        "endpoints": ["/health", "/rewrite"],
    }
