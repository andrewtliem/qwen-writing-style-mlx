# Fine-Tune Qwen for Writing Style with MLX

This repository is a local tutorial for fine-tuning a Qwen model on Apple Silicon with MLX, then serving the resulting adapter through FastAPI and a simple browser UI.

The tutorial is based on your `qwen_mlx_tutorial.docx` outline and the dataset examples in [`newData`](/Users/andrewtannyliem/Documents/qwen-lora/newData).

## Tutorial Goal

The goal is style transfer, not knowledge injection.

In this repo, the target behavior is:

- take technical EPON writing as input
- rewrite it in a more formal academic paper style
- preserve the original technical meaning

## Repo Structure

- [`app.py`](/Users/andrewtannyliem/Documents/qwen-lora/app.py): FastAPI wrapper around `mlx_lm.generate`
- [`rewrite_frontend.html`](/Users/andrewtannyliem/Documents/qwen-lora/rewrite_frontend.html): browser playground for the fine-tuned adapter
- [`Modelfile`](/Users/andrewtannyliem/Documents/qwen-lora/Modelfile): model wrapper configuration for the adapter
- [`newData/train.jsonl`](/Users/andrewtannyliem/Documents/qwen-lora/newData/train.jsonl): training split
- [`newData/valid.jsonl`](/Users/andrewtannyliem/Documents/qwen-lora/newData/valid.jsonl): validation split
- [`newData/test.jsonl`](/Users/andrewtannyliem/Documents/qwen-lora/newData/test.jsonl): test split

Current split sizes:

- train: 180 examples
- valid: 30 examples
- test: 30 examples

## 1. Requirements

This workflow assumes:

- Apple Silicon Mac
- Python virtual environment
- `mlx-lm` installed
- a Qwen instruct base model, such as `mlx-community/Qwen2.5-0.5B-Instruct-4bit`

Install the API and inference dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install mlx-lm
```

## 2. Dataset Design

The dataset should contain rewrite pairs, not QA pairs.

The intended pattern from your tutorial doc is:

- input: simpler or rough technical writing
- output: improved academic wording in your target paper style

Good tasks for this setup:

- paraphrase pairs
- rewrite pairs
- paragraph improvement pairs

## 3. Actual Dataset Format in `newData`

Your current dataset uses MLX-friendly chat examples in JSONL format. Each line has a `messages` array with one `user` message and one `assistant` message.

Example structure:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Rewrite the following in my academic EPON paper style. Avoid generic or business phrases and focus on technical clarity:\n\nThere are online and offline DBA approaches, and each has strengths and weaknesses."
    },
    {
      "role": "assistant",
      "content": "In this paper, one of the objectives is to improve overall QoS, particularly for P2P live streaming. QoS performance can be characterized with several parameters, such as packet delay, jitter, system throughput, and packet loss ratio."
    }
  ]
}
```

That schema is structurally valid for training, but content quality still matters more than format.

## 4. Important Dataset Quality Note

Your docx correctly says dataset quality matters more than hyperparameters. The examples in `newData` support that point directly.

Some rows are good:

- input and output are aligned
- the assistant keeps the same meaning
- the rewrite is more formal or technically precise

Some rows are noisy:

- the assistant output changes the topic
- the assistant output does not preserve the input meaning
- some rows are effectively identity rewrites

For example, several samples in `train.jsonl` ask about one topic and answer with text from a different EPON context. That kind of mismatch will teach the model unstable behavior.

Before retraining, clean the dataset so each pair satisfies all three rules:

1. Same technical meaning.
2. Better academic phrasing.
3. No unrelated topic drift.

## 5. Training Command

Your docx uses this MLX LoRA pattern:

```bash
mlx_lm.lora \
  --model mlx-community/Qwen2.5-0.5B-Instruct-4bit \
  --train \
  --data ./newData \
  --adapter-path ./qwen25_v8 \
  --iters 300 \
  --batch-size 1 \
  --grad-accumulation-steps 8 \
  --num-layers 6 \
  --learning-rate 3e-6 \
  --max-seq-length 512
```

Notes:

- I changed `--data ./data_v8` from the docx to `--data ./newData` because that is the dataset folder present in this repo.
- `./qwen25_v8` matches the adapter naming already referenced by the app.
- If your installed `mlx-lm` version exposes training through a slightly different CLI entrypoint, keep the same arguments but use the command name from your local version.

## 6. Evaluation

Your tutorial outline says to compare the base model against the fine-tuned model. That is the right evaluation target for this project.

Check for:

- more technical tone
- reduced generic wording
- preserved meaning
- more consistent EPON-style phrasing

Practical evaluation method:

1. Pick 10 to 20 held-out inputs from [`newData/test.jsonl`](/Users/andrewtannyliem/Documents/qwen-lora/newData/test.jsonl).
2. Generate outputs with the base model only.
3. Generate outputs again with the adapter.
4. Compare whether the adapter improves style without inventing unrelated content.

## 7. Deployment

This repo already contains the local deployment layer.

The FastAPI service in [`app.py`](/Users/andrewtannyliem/Documents/qwen-lora/app.py) calls `mlx_lm.generate` with:

- `MLX_BASE_MODEL`
- `MLX_ADAPTER_PATH`
- generation parameters from the request

Start the API with:

```bash
uvicorn app:app --reload
```

Default local endpoint:

- `http://127.0.0.1:8000`

Useful routes:

- `GET /`
- `GET /health`
- `POST /rewrite`
- `GET /docs`

## 8. Browser Demo

Open [`rewrite_frontend.html`](/Users/andrewtannyliem/Documents/qwen-lora/rewrite_frontend.html) in a browser after the API is running.

The page is now set up as a tutorial playground:

- setup reminder at the top
- direct input/output comparison
- adjustable generation parameters
- sample EPON sentences for quick testing

## 9. Environment Variables

The app reads these values:

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

## 10. API Test Example

You can test the fine-tuned model without the frontend:

```bash
curl -X POST http://127.0.0.1:8000/rewrite \
  -H "Content-Type: application/json" \
  -d '{
    "text": "This scheduling method lowers delay and improves channel usage, especially when the network is heavily loaded.",
    "instruction": "Rewrite the following in a formal EPON research paper style. Avoid generic or business phrases and focus on technical clarity.",
    "max_tokens": 180,
    "temperature": 0.3,
    "top_p": 0.9
  }'
```

## 11. Key Lessons from This Tutorial

The points from your docx hold up after looking at the actual dataset:

- dataset quality matters more than hyperparameter tweaking
- rewrite-style supervision is the correct setup for writing-style transfer
- prompts should stay consistent across train and inference
- overfitting is a real risk on a small dataset
- noisy rewrite pairs will reduce output reliability

## 12. Recommended Next Cleanup

The next high-value improvement is not a code change. It is dataset cleaning.

Specifically:

1. Remove rows where the output changes topic.
2. Remove rows where the output does not preserve the input meaning.
3. Keep only examples that genuinely rewrite the same content in your target style.
4. Retrain after cleaning, then compare base vs fine-tuned outputs again.
