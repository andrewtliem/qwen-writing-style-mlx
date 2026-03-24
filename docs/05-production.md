# 🚀 05 Production

## From Experiment to Daily Use

This repo includes a small local deployment layer so the fine-tuned model can be used as a practical academic paraphrasing tool.

The production goal is narrow on purpose:

- accept a rewrite request
- apply a fixed academic-style instruction
- return a cleaner paraphrase through a simple interface

## 🔌 API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Default local endpoint:

```text
http://127.0.0.1:8000
```

Useful routes:

- `GET /`
- `GET /health`
- `POST /rewrite`
- `GET /docs`

## 🧠 Why a Custom FastAPI Wrapper

For this use case, a custom wrapper is easier to control than a generic chat-serving layer.

It gives you direct control over:

- the fixed rewrite instruction
- adapter path selection
- request validation
- generation limits
- the response shape used by the frontend

That is useful when the audience is lecturers or researchers who just want a reliable rewrite tool.

## 🌱 Environment Variables

The app reads:

- `MLX_BASE_MODEL`
- `MLX_ADAPTER_PATH`
- `MLX_BIN`
- `MAX_INPUT_CHARS`
- `DEFAULT_MAX_TOKENS`
- `DEFAULT_TEMP`
- `DEFAULT_TOP_P`

Example:

```bash
export MLX_BASE_MODEL=mlx-community/Qwen2.5-0.5B-Instruct-4bit
export MLX_ADAPTER_PATH=/absolute/path/to/your/adapter
uvicorn app:app --reload
```

## 🖥️ Frontend

Use the browser UI at [`frontend/rewrite_frontend.html`](../frontend/rewrite_frontend.html) after the API is running.

The page provides:

- input/output comparison
- generation controls
- sample technical inputs
- a short guided flow for local testing

## 📌 Production Lessons

- keep the task narrow
- keep the prompt consistent with training
- expose only the parameters you actually want to tune
- prefer a simple local system before expanding to more infrastructure

## 👩‍🏫 Real-World Use

For a lecturer, the practical workflow is straightforward:

1. paste a paragraph from notes, a draft, or a paper section
2. run the rewrite
3. review the paraphrase
4. keep, edit, or reject the output

That is the right mindset for this tool. It should support academic writing, not replace academic judgment.
