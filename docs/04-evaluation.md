# 🔍 04 Evaluation

## What You Should Evaluate

This tutorial is not about factual QA accuracy. It is about writing behavior.

The model should:

- sound more academic
- reduce generic wording
- preserve technical meaning
- stay on topic
- remain stable across similar prompts

## ⚖️ Compare the Right Things

Always compare:

- base model output
- fine-tuned model output

Use the same prompts for both. Otherwise, the comparison is not useful.

## ✅ Practical Evaluation Flow

1. Take held-out inputs from [`data/test.jsonl`](../data/test.jsonl).
2. Generate outputs with the base model only.
3. Generate outputs again with the adapter enabled.
4. Record the results in [`examples/base_vs_finetuned.md`](../examples/base_vs_finetuned.md).

## 🧠 Main Lesson

Lower training loss is not automatically better.

One of the biggest lessons from this project was that the best qualitative behavior appeared before deep overfitting. A later checkpoint can have lower loss while producing less reliable paraphrases.

That means checkpoint selection should be based on side-by-side output review, not only training metrics.

## 🚩 Failure Signs

- topic drift
- unrelated claims
- details added that were not present in the input
- little or no style improvement
- polished wording that still changes the meaning

## ❌ What Did Not Work

- assuming lower loss always meant better style transfer
- evaluating only on training metrics
- ignoring small meaning shifts because the output sounded more academic

## 👩‍🏫 Academic Review Tip

If the target user is a lecturer or researcher, one of the best tests is simple:

Would you be comfortable placing the rewritten sentence into your own notes, slides, or paper draft after a light review?

If the answer is no, the model is not ready yet.
