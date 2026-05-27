# QualityForge 使用指南

> 自我改进质量系统——让AI自动学习、评分、重生成，持续进化

---

## 核心概念

QualityForge 是一个**自我改进质量系统**，它的核心理念是：AI的输出质量不应该只靠人工评估，而应该建立自动化的"评分→反馈→改进→再评分"循环，实现持续自我进化。

**为什么重要？**

传统AI系统的质量改进依赖人工反馈：
1. 人工评估输出质量（耗时、主观）
2. 根据反馈调整Prompt（依赖经验）
3. 再次测试（循环慢、效率低）

QualityForge 将这个过程自动化：
```
生成输出 → 自动评分 → 不足则重生成 → 记录成功模式 → 持续优化
```

每次执行都成为学习的机会，系统会越来越聪明。

---

## 如何使用

### 第一步：定义质量评分标准

```python
from qualityforge import QualitySystem, Criteria

# 定义评分维度
criteria = [
    Criteria(name="准确性", weight=0.4, metric="factual"),
    Criteria(name="完整性", weight=0.2, metric="coverage"),
    Criteria(name="清晰度", weight=0.2, metric="clarity"),
    Criteria(name="实用性", weight=0.2, metric="actionability")
]

quality_system = QualitySystem(criteria=criteria)
```

### 第二步：自动评分与改进

```python
# 生成初始输出
output = await nexuscore.route(prompt)

# 质量评分
score = await quality_system.evaluate(output, context=prompt)

if score.overall < 0.8:
    # 质量不达标，自动重生成
    feedback = score.get_detailed_feedback()

    improved_output = await quality_system.regenerate(
        prompt=prompt,
        feedback=feedback,
        max_attempts=3
    )

    # 再次评分确认
    final_score = await quality_system.evaluate(improved_output, context=prompt)
```

### 第三步：积累学习模式

```python
# QualityForge自动记录成功模式
quality_system.learn_from_success(
    prompt_pattern="分析XXX类问题",
    successful_approach="分三步：1.识别特征 2.对比数据 3.给出结论",
    score=0.95
)

# 下次遇到类似问题，自动应用成功模式
```

---

## 代码示例

```python
import asyncio
from qualityforge import QualitySystem, AutoImprover

async def intelligent_agent_loop():
    qs = QualitySystem()
    improver = AutoImprover(qs, learning_rate=0.1)

    prompts = [
        "解释量子纠缠原理",
        "分析新能源汽车市场趋势",
        "设计用户登录功能"
    ]

    for prompt in prompts:
        # 自动生成+评分+改进循环
        best_output = await improver.optimize(
            prompt=prompt,
            max_iterations=5,
            target_score=0.85
        )

        print(f"最终得分: {best_output.score}")
        print(f"迭代次数: {best_output.iterations}")
        print(f"输出: {best_output.content[:100]}...")

asyncio.run(intelligent_agent_loop())
```

---

## 适用场景

### 场景1：对话机器人持续优化
客服机器人每次对话后自动评分，不达标的对话自动重生成。系统从成功对话中学习什么回复最有效，持续提升客服质量。

### 场景2：代码生成质量控制
AI生成的代码通过QualityForge评分：正确性、可读性、性能、安全性。低于标准的代码自动重新生成，直到达到生产级标准。

### 场景3：内容创作流水线
营销文案生成后，自动评估：品牌调性匹配度、转化率预测、语法正确性。自动优化直到达到专业水准。

### 场景4：研究报告质量保障
投研报告生成后，自动检查：数据准确性、逻辑完整性、结论可靠性。发现问题自动重写，直到通过质量门禁。

---

## 与其他模块的关系

| 模块 | 关系 | 说明 |
|:----:|:----:|:-----|
| TruthMatrix | 评分输入 | TruthMatrix的验证结果作为QualityForge的评分依据 |
| NexusCore | 执行引擎 | QualityForge通过NexusCore重新生成并验证 |
| AgentHive | 质量协调 | AgentHive中的Agent表现由QualityForge持续评分 |
| SelfMend | 质量问题触发 | 持续的质量问题会触发SelfMend的系统级修复 |

**架构定位**：QualityForge是持续改进层，将质量控制从人工变成自动化，是系统进化的核心驱动。

---

## 评分报告示例

```python
report = await qs.evaluate(output, context)

print(f"""
质量报告
========
总分: {report.overall_score:.1%}

维度详情:
  准确性: {report.scores.accuracy:.1%} {'✅' if report.scores.accuracy > 0.8 else '⚠️'}
  完整性: {report.scores.completeness:.1%} {'✅' if report.scores.completeness > 0.8 else '⚠️'}
  清晰度: {report.scores.clarity:.1%} {'✅' if report.scores.clarity > 0.8 else '⚠️'}
  实用性: {report.scores.actionability:.1%} {'✅' if report.scores.actionability > 0.8 else '⚠️'}

改进建议:
{report.improvement_suggestions}

学习记录:
  模式库大小: {qs.pattern_count}
  平均质量: {qs.avg_quality:.1%}
""")
```

---

## 下一步

- 查看 [TruthMatrix 指南](./truthmatrix-guide.md) — 了解底层验证机制
- 查看 [SelfMend 指南](./selfmend-guide.md) — 如何处理持续的质量问题
- 开始集成：pip install qualityforge

---

*QualityForge — 让AI从"尽力做好"升级为"越来越好"*