# QualityForge User Guide

> Self-Improving Quality System — Let AI Automatically Learn, Score, Regenerate, and Evolve Continuously

---

## Core Concept

QualityForge is a **self-improving quality system** whose core philosophy is: AI output quality shouldn't rely solely on human evaluation. Instead, build an automated "score → feedback → improve → re-score" loop to achieve continuous self-evolution.

**Why does it matter?**

Traditional AI system quality improvement relies on human feedback:
1. Human evaluates output quality (time-consuming, subjective)
2. Adjust Prompt based on feedback (relies on experience)
3. Test again (slow cycle, low efficiency)

QualityForge automates this process:
```
Generate output → Auto-score → Below standard? Regenerate → Record successful patterns → Continuously optimize
```

Every execution becomes a learning opportunity. The system gets smarter over time.

---

## How to Use

### Step 1: Define Quality Scoring Criteria

```python
from qualityForge import QualitySystem, Criteria

# Define scoring dimensions
criteria = [
    Criteria(name="Accuracy", weight=0.4, metric="factual"),
    Criteria(name="Completeness", weight=0.2, metric="coverage"),
    Criteria(name="Clarity", weight=0.2, metric="clarity"),
    Criteria(name="Actionability", weight=0.2, metric="actionability")
]

quality_system = QualitySystem(criteria=criteria)
```

### Step 2: Auto-Score and Improve

```python
# Generate initial output
output = await nexuscore.route(prompt)

# Quality scoring
score = await quality_system.evaluate(output, context=prompt)

if score.overall < 0.8:
    # Quality below standard, auto-regenerate
    feedback = score.get_detailed_feedback()

    improved_output = await quality_system.regenerate(
        prompt=prompt,
        feedback=feedback,
        max_attempts=3
    )

    # Score again to confirm
    final_score = await quality_system.evaluate(improved_output, context=prompt)
```

### Step 3: Accumulate Learning Patterns

```python
# QualityForge automatically records successful patterns
quality_system.learn_from_success(
    prompt_pattern="Analyze XXX-type problems",
    successful_approach="Three steps: 1. Identify features 2. Compare data 3. Draw conclusions",
    score=0.95
)

# Next time encountering similar problems, automatically apply successful patterns
```

---

## Code Example

```python
import asyncio
from qualityForge import QualitySystem, AutoImprover

async def intelligent_agent_loop():
    qs = QualitySystem()
    improver = AutoImprover(qs, learning_rate=0.1)

    prompts = [
        "Explain quantum entanglement",
        "Analyze new energy vehicle market trends",
        "Design user login functionality"
    ]

    for prompt in prompts:
        # Auto-generate + score + improve loop
        best_output = await improver.optimize(
            prompt=prompt,
            max_iterations=5,
            target_score=0.85
        )

        print(f"Final score: {best_output.score}")
        print(f"Iterations: {best_output.iterations}")
        print(f"Output: {best_output.content[:100]}...")

asyncio.run(intelligent_agent_loop())
```

---

## Use Cases

### Case 1: Continuous Optimization of Chatbots
Customer service bot auto-scores after every conversation. Substandard conversations auto-regenerate. System learns from successful conversations what responses are most effective, continuously improving service quality.

### Case 2: Code Generation Quality Control
AI-generated code is scored by QualityForge: correctness, readability, performance, security. Substandard code auto-regenerates until reaching production-grade quality.

### Case 3: Content Creation Pipeline
Marketing copy is auto-evaluated after generation: brand tone match, conversion rate prediction, grammar correctness. Auto-optimizes until reaching professional standards.

### Case 4: Research Report Quality Assurance
After investment research reports are generated, automatically check: data accuracy, logical completeness, conclusion reliability. Problems trigger automatic rewrite until passing quality gate.

---

## Relationship with Other Modules

| Module | Relationship | Description |
|:----:|:----:|:-----|
| TruthMatrix | Scoring Input | TruthMatrix validation results serve as QualityForge scoring basis |
| NexusCore | Execution Engine | QualityForge regenerates and validates via NexusCore |
| AgentHive | Quality Coordination | Agent performance in AgentHive is continuously scored by QualityForge |
| SelfMend | Quality Issue Trigger | Persistent quality issues trigger SelfMend system-level repair |

**Architecture Position**: QualityForge is the continuous improvement layer, transforming quality control from manual to automated — the core driver of system evolution.

---

## Scoring Report Example

```python
report = await qs.evaluate(output, context)

print(f"""
Quality Report
========
Overall Score: {report.overall_score:.1%}

Dimension Details:
  Accuracy: {report.scores.accuracy:.1%} {'✅' if report.scores.accuracy > 0.8 else '⚠️'}
  Completeness: {report.scores.completeness:.1%} {'✅' if report.scores.completeness > 0.8 else '⚠️'}
  Clarity: {report.scores.clarity:.1%} {'✅' if report.scores.clarity > 0.8 else '⚠️'}
  Actionability: {report.scores.actionability:.1%} {'✅' if report.scores.actionability > 0.8 else '⚠️'}

Improvement Suggestions:
{report.improvement_suggestions}

Learning Records:
  Pattern Library Size: {qs.pattern_count}
  Average Quality: {qs.avg_quality:.1%}
""")
```

---

## Next Steps

- See the [TruthMatrix Guide](./truthmatrix-guide_en.md) — Understanding the underlying validation mechanism
- See the [SelfMend Guide](./selfmend-guide_en.md) — How to handle persistent quality issues
- Get started: `pip install qualityForge`

---

*QualityForge — Upgrade AI from "try your best" to "getting better and better"*
