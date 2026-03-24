# 02 Dataset Design

The dataset should contain rewrite pairs, not question-answer pairs.

Target pattern:

- user message: rough, plain, or less formal technical writing
- assistant message: rewritten version in the target academic style

Recommended data types:

- paraphrase pairs
- rewrite pairs
- paragraph improvement pairs

## Current Format

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

## Current Split

- train: 180 examples
- valid: 30 examples
- test: 30 examples

## Quality Rules

Every pair should satisfy all of these:

1. Preserve the same technical meaning.
2. Improve the wording or tone.
3. Stay on the same topic.

Some existing rows are noisy and should be cleaned before retraining because mismatched pairs will teach unstable behavior.
