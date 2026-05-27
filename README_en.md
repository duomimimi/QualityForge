# QualityForge

**Self-Improving Quality System for AI Outputs**

QualityForge is an automated quality assurance framework that scores AI output quality, automatically regenerates failed outputs, and continuously learns from mistakes. It treats quality as a feedback loop, not a one-time check.

## Key Features

- **Auto-Scoring**: Automatically evaluate outputs across multiple quality dimensions (accuracy, clarity, coherence, safety)
- **Auto-Regeneration**: When quality falls below threshold, automatically regenerate with refined prompts
- **Learning from Mistakes**: Build a mistake pattern library that improves future generations
- **Quality Baselines**: Define minimum quality thresholds per use case
- **Multi-Dimensional Scoring**: Score not just overall quality but broken down by dimension
- **Continuous Improvement**: Each iteration improves the underlying generation strategy

## Quick Start

```bash
# Install
pip install qualityforge

# Basic usage
from qualityforge import QualityForge, QualityStandard

forge = QualityForge(config={
    "quality_threshold": 0.85,
    "max_retries": 3,
    "dimensions": ["accuracy", "clarity", "safety"]
})

standard = QualityStandard(
    accuracy_weight=0.4,
    clarity_weight=0.3,
    safety_weight=0.3
)

result = forge.generate_and_score(
    prompt="Write a technical blog post about distributed systems",
    standard=standard
)

# Auto-regenerates if quality < threshold
print(result.score, result.regenerations_used)
```

## Architecture

```
┌─────────────────────────────────────────────┐
│           Generation Request                 │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│         QualityForge Engine                  │
│  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Prompt   │  │    Generator         │  │
│  │   Builder   │  │   (AI Model)         │  │
│  └─────────────┘  └─────────────────────┘  │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│          Quality Scorer                      │
│  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Multi-Dim  │  │   Pass/Fail         │  │
│  │   Scoring   │  │   Threshold         │  │
│  └─────────────┘  └─────────────────────┘  │
└─────────────────────┬───────────────────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
     ┌─────────┐           ┌─────────────┐
     │ Pass    │           │ Fail → Retry│
     │ Output  │           │ (Refine)    │
     └─────────┘           └─────────────┘
          │                       │
          │                       │
          └───────────┬───────────┘
                      ▼
┌─────────────────────────────────────────────┐
│        Mistake Pattern Library               │
│    (Improves Future Generations)            │
└─────────────────────────────────────────────┘
```

**Core Components:**

- **Prompt Builder**: Crafts and refines generation prompts
- **Quality Scorer**: Multi-dimensional automatic evaluation
- **Regeneration Loop**: Auto-retries with refined prompts on failure
- **Mistake Library**: Stores patterns of failures for learning
- **Strategy Optimizer**: Updates generation strategies based on feedback

## License

MIT License