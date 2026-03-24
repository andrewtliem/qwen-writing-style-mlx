# 05 Production

This repo includes a local inference and demo layer.

## API

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

## Environment Variables

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

## Frontend

Use the browser UI at [`frontend/rewrite_frontend.html`](/Users/andrewtannyliem/Documents/qwen-lora/frontend/rewrite_frontend.html) after the API is running.

The page provides:

- input/output comparison
- generation controls
- sample EPON inputs
- a short tutorial flow for local testing
