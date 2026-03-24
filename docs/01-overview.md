# 🎯 01 Overview

## What You Are Building

This project fine-tunes a Qwen instruct model with MLX so it can paraphrase technical writing in your own academic style.

The goal is not to teach the model everything about EPON. The goal is narrower and more practical:

- give it technical text
- ask it to rewrite that text in a formal academic voice
- preserve the original meaning

That framing is important because it changes how you design the dataset, how you evaluate the model, and how you deploy it.

## 👩‍🏫 Why This Matters for Lecturers

Many lecturers and researchers do not want a generic AI assistant. They want a writing tool that helps them:

- revise paragraphs without losing their academic tone
- paraphrase lecture notes and research drafts
- make wording more formal and publication-ready
- stay stylistically consistent across documents

This tutorial is built around that use case.

## 🧱 Main Components

- [`app.py`](../app.py) — FastAPI wrapper around `mlx_lm.generate`
- [`frontend/rewrite_frontend.html`](../frontend/rewrite_frontend.html) — local browser playground
- [`data/train.jsonl`](../data/train.jsonl) — training split
- [`data/valid.jsonl`](../data/valid.jsonl) — validation split
- [`data/test.jsonl`](../data/test.jsonl) — test split

## 🔄 Workflow at a Glance

1. Build rewrite-style training examples.
2. Fine-tune a Qwen instruct model with MLX LoRA.
3. Compare the base model and the fine-tuned model on the same prompts.
4. Serve the adapter through a small local API.
5. Test it from the browser with real academic sentences.

## ✅ Prerequisites

- Apple Silicon Mac
- Python virtual environment
- `mlx-lm`
- access to the target model on Hugging Face
- a small instruct model already available in MLX format

The model used in this tutorial is:

```text
mlx-community/Qwen2.5-0.5B-Instruct-4bit
```

## 🧠 Why an Instruct Model

One of the biggest practical lessons from the project was model choice.

- small base models were unstable
- the instruct model was the first option that produced usable rewrite behavior
- after that, dataset quality became the main bottleneck

That is why this tutorial is centered on a Qwen instruct model rather than a base model.

## ⚠️ What Did Not Work

The tutorial is more useful when the failures are explicit.

- tiny base models produced unstable outputs
- generic QA-style data did not transfer writing style well
- very low training loss did not automatically mean better results
- overly generic deployment paths did not match the narrow rewrite use case as cleanly as a custom wrapper
