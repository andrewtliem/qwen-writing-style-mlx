# 01 Overview

This project fine-tunes a Qwen instruct model with MLX to learn a writing style rather than teach new knowledge.

In this repo, the target task is:

- take technical EPON text as input
- rewrite it in a more formal academic style
- preserve the original technical meaning

Core components:

- [`app.py`](/Users/andrewtannyliem/Documents/qwen-lora/app.py): FastAPI wrapper around `mlx_lm.generate`
- [`frontend/rewrite_frontend.html`](/Users/andrewtannyliem/Documents/qwen-lora/frontend/rewrite_frontend.html): browser playground
- [`data/train.jsonl`](/Users/andrewtannyliem/Documents/qwen-lora/data/train.jsonl): training split
- [`data/valid.jsonl`](/Users/andrewtannyliem/Documents/qwen-lora/data/valid.jsonl): validation split
- [`data/test.jsonl`](/Users/andrewtannyliem/Documents/qwen-lora/data/test.jsonl): test split

The workflow is simple:

1. Build rewrite-style examples.
2. Train a LoRA adapter with MLX.
3. Compare the base model against the fine-tuned model.
4. Serve the adapter locally through FastAPI.
5. Test the model from the browser UI or API.
