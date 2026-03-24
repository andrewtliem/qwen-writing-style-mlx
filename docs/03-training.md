# ⚙️ 03 Training

## Training Goal

The goal of training is not to create a broad assistant. It is to create a focused academic paraphrasing model that behaves consistently on your writing tasks.

## 🛠️ Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install mlx-lm
```

## 🤖 Base Model

Example base model:

```text
mlx-community/Qwen2.5-0.5B-Instruct-4bit
```

This choice was based on experiment results, not preference alone.

- earlier small base-style models were less stable
- the instruct variant produced the first usable rewrite behavior
- once model stability improved, dataset quality became the main factor

## ▶️ Training Command

```bash
mlx_lm.lora \
  --model mlx-community/Qwen2.5-0.5B-Instruct-4bit \
  --train \
  --data ./data \
  --adapter-path ./qwen25_v8 \
  --iters 300 \
  --batch-size 1 \
  --grad-accumulation-steps 8 \
  --num-layers 6 \
  --learning-rate 3e-6 \
  --max-seq-length 512
```

## 📌 Practical Notes

- `--data ./data` points to the dataset folder used in this tutorial
- `./qwen25_v8` is the adapter path referenced by the app
- if your `mlx-lm` version uses a different training entrypoint, keep the arguments and adjust only the command name

## 🧠 How to Think About Training

- keep the task narrow and consistent
- do not expect hyperparameter changes to rescue a weak dataset
- validation behavior matters more than the lowest possible training loss
- the best checkpoint may appear before the most overfit checkpoint

## ⚠️ Common Mistake

A lower loss curve can look impressive while the output quality quietly gets worse.

For this use case, the real question is:

Does the model paraphrase in your academic style while preserving meaning?

That question matters more than a single training metric.
