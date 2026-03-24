# 🧪 02 Dataset Design

## The Golden Rule

If the goal is academic paraphrasing, the dataset must look like academic paraphrasing.

That means the dataset should contain rewrite pairs, not generic question-answer pairs.

## ✅ Target Pattern

- user message — rough, plain, or less formal technical writing
- assistant message — the same idea rewritten in the target academic style

Good example types:

- paraphrase pairs
- rewrite pairs
- paragraph improvement pairs

## 💡 Why Dataset Design Mattered Most

The strongest lesson from this project was not about hyperparameters. It was about task alignment.

The model improved when the data matched the real use case:

- input — weaker or rougher technical writing
- output — the same meaning expressed in a stronger academic voice

When the dataset drifted toward explanation or unrelated answer generation, the model drifted too.

## 📈 Dataset Evolution

The tutorial becomes much more useful when the dataset changes are shown honestly:

- `v1` — explanation-only dataset
- `v2` — more examples, but still weak task alignment
- `v3` — paragraph-style data
- `v6` and `v7` — rewrite/paraphrase style became the main direction
- `v8` — cleaner train, validation, and test split

This progression shows the real turning point: the data became better aligned with the actual paraphrasing task.

## 🧩 Current Format

Each JSONL row uses a `messages` array:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Rewrite the following in my academic EPON paper style..."
    },
    {
      "role": "assistant",
      "content": "Rewritten output in the target style..."
    }
  ]
}
```

## 📊 Current Split

- train — 180 examples
- valid — 30 examples
- test — 30 examples

## 📝 Quality Rules

Every example should satisfy all three rules:

1. Preserve the original technical meaning.
2. Improve the wording or tone.
3. Stay on the same topic.

Even a small number of noisy pairs can teach unstable behavior, especially on a small dataset.

## 🧹 What to Clean Before Retraining

Remove or rewrite rows with these problems:

- the output changes topic
- the output adds claims that were not in the input
- the output keeps nearly the same wording without meaningful improvement
- the output sounds academic but does not preserve the original meaning

## 🎓 Academic Writing Tip

If you are preparing this for lecturers, the best data usually comes from:

- your own before-and-after revisions
- informal sentences rewritten into journal style
- paragraphs revised for clarity, precision, and tone

That kind of data teaches style much better than generic instruction-following examples.
