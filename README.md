# 🎓 qwen-writing-style-mlx

Fine-tune a small Qwen model with MLX so it can paraphrase technical writing in your own academic style.

This project is designed for lecturers, researchers, and academic writers who want a narrow writing assistant, not a general chatbot. The goal is simple: give the model a sentence or paragraph, and have it rewrite the text in a more formal academic voice while preserving the original meaning.

## ✨ Why This Project Is Useful

- paraphrase your own technical sentences in a style that sounds closer to your papers
- revise lecture material, journal drafts, and research notes more consistently
- keep the workflow local on Apple Silicon
- serve the model through a simple API and browser UI

## 🧭 What You Will Build

By the end of this tutorial, you will have:

- a LoRA fine-tuned Qwen instruct model
- a dataset of rewrite-style examples
- a FastAPI wrapper for local inference
- a simple frontend for testing paraphrases
- a repeatable workflow for academic writing-style transfer

## 👩‍🏫 Who This Tutorial Is For

- lecturers who want AI assistance without losing their own writing identity
- researchers who want more consistent academic paraphrasing
- students or assistants building a focused academic writing tool
- practitioners learning MLX fine-tuning through a real use case

## 🗂️ Project Structure

```text
qwen-writing-style-mlx/
├── README.md
├── requirements.txt
├── app.py
├── frontend/
│   └── rewrite_frontend.html
├── data/
│   ├── train.jsonl
│   ├── valid.jsonl
│   └── test.jsonl
├── docs/
│   ├── 01-overview.md
│   ├── 02-dataset-design.md
│   ├── 03-training.md
│   ├── 04-evaluation.md
│   └── 05-production.md
└── examples/
    ├── base_vs_finetuned.md
    └── prompts.md
```

## 🚀 Quick Start

### 1. Create the environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install mlx-lm
```

### 2. Start the API

```bash
uvicorn app:app --reload
```

### 3. Open the browser UI

Use [`frontend/rewrite_frontend.html`](/Users/andrewtannyliem/Documents/qwen-lora/frontend/rewrite_frontend.html) to test the paraphrasing flow.

## 📚 Documentation

- [`docs/01-overview.md`](/Users/andrewtannyliem/Documents/qwen-lora/docs/01-overview.md) — what you are building and why
- [`docs/02-dataset-design.md`](/Users/andrewtannyliem/Documents/qwen-lora/docs/02-dataset-design.md) — how to design rewrite-style training data
- [`docs/03-training.md`](/Users/andrewtannyliem/Documents/qwen-lora/docs/03-training.md) — MLX LoRA training workflow
- [`docs/04-evaluation.md`](/Users/andrewtannyliem/Documents/qwen-lora/docs/04-evaluation.md) — how to compare base vs fine-tuned outputs
- [`docs/05-production.md`](/Users/andrewtannyliem/Documents/qwen-lora/docs/05-production.md) — how to serve the model locally

## 💡 Core Idea

This tutorial is valuable because it is honest about the real lesson:

- better dataset design mattered more than chasing lower loss
- instruct models behaved better than small base models
- rewrite-style supervision matched the real use case better than generic QA data

If your goal is academic paraphrasing in your own voice, that is the part that matters most.
