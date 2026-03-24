# Base vs Fine-Tuned

This page records a simple side-by-side comparison between a more AI-sounding rewrite and a cleaner fine-tuned rewrite.

## Example 1

### Base-style output

![Base model GPTZero result](images/base-model.png)

```text
P2P live streaming works by letting users share the load with each other instead of relying on a single server. Each peer not only receives video chunks but also forwards them to others, helping distribute the stream across the network. These connected peers form what is called a swarm, which is created dynamically as each user chooses whom to connect with. Because everything depends on these peer-to-peer connections, network factors like jitter, delay, and throughput play a major role in determining the overall quality of service (QoS), affecting how smooth and timely the streaming experience is.
```

Observed result from the provided screenshot:

- GPTZero scan flagged the text as `AI 100%`

### Fine-tuned output

![Fine-tuned model GPTZero result](images/fine-tuned-model.png)

```text
P2P live streaming is a decentralized technology that enables users to share the load among themselves rather than relying on a single server. Each peer in the network receives video chunks and forwards them to other peers. This allows the live streaming stream to be distributed across the network, thereby increasing the capacity and bandwidth of the network. The connected peers form a swarm, which is created dynamically based on each user's choice of connection. The quality of the live streaming experience is influenced by the factors of jitter, delay, and throughput.
```

Observed result from the provided screenshot:

- GPTZero scan labeled the text as `Human 99%`

### Notes

- The fine-tuned version is shorter and more controlled.
- The sentence structure is less obviously "LLM-explanatory" than the base-style version.
- The rewritten paragraph still needs human review, but it reads closer to edited academic prose.
- The detector result is only one external signal, not proof of writing quality by itself.
