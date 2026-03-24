# qwen-writing-style-mlx

Tutorial repo for fine-tuning Qwen with MLX for academic writing-style transfer, then serving the adapter through FastAPI.

## Structure

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

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install mlx-lm
uvicorn app:app --reload
```

Then open [`frontend/rewrite_frontend.html`](/Users/andrewtannyliem/Documents/qwen-lora/frontend/rewrite_frontend.html).

## Documentation

- [`docs/01-overview.md`](/Users/andrewtannyliem/Documents/qwen-lora/docs/01-overview.md)
- [`docs/02-dataset-design.md`](/Users/andrewtannyliem/Documents/qwen-lora/docs/02-dataset-design.md)
- [`docs/03-training.md`](/Users/andrewtannyliem/Documents/qwen-lora/docs/03-training.md)
- [`docs/04-evaluation.md`](/Users/andrewtannyliem/Documents/qwen-lora/docs/04-evaluation.md)
- [`docs/05-production.md`](/Users/andrewtannyliem/Documents/qwen-lora/docs/05-production.md)

## Notes

- `data/` is sourced from the dataset examples that were previously in `newData/`.
- `examples/` is reserved for your own comparison outputs and prompt references.
