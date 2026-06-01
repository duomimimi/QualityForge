# QualityForge - Self-Improving Quality System

## 核心能力

QualityForge是一个**自优化的AI质量系统**，核心能力：

1. **自动评分**：无需人工标注，自动评估输出质量
2. **自动修正**：发现低质量内容，自动重生成
3. **持续学习**：从修正中学习，提升未来表现

## 质量维度

QualityForge从多个维度评估质量：

| 维度 | 说明 | 权重 |
|:-----|:-----|:-----|
| 准确性 | 输出是否正确 | 30% |
| 完整性 | 是否覆盖所有要点 | 20% |
| 流畅性 | 文字是否流畅 | 15% |
| 相关性 | 是否切题 | 25% |
| 安全性 | 是否有害/不当内容 | 10% |

## 自动评分流程

`
输入 -> 质量检测 -> 评分引擎 -> 输出评分
                      │
                      ▼
                ┌─────────────┐
                │ 质量阈值    │ -> 低于阈值触发重生成
                └─────────────┘
`

## 自学习机制

QualityForge从每次修正中学习：

`python
class LearningEngine:
    def learn_from_correction(self, original, regenerated):
        # 分析原版vs重生成版的差异
        diff = self.analyze_diff(original, regenerated)
        
        # 提取成功的修正模式
        successful_patterns = diff.extract_successful_patterns()
        
        # 更新质量评分模型
        self.quality_model.update(successful_patterns)
`

## 与其他模块集成

| 模块 | 关系 |
|:----:|:-----|
| TruthMatrix | QualityForge使用TruthMatrix验证输出质量 |
| NexusCore | QualityForge通过NexusCore路由到最优模型 |
| SelfMend | SelfMend监控QualityForge的健康状态 |

---

*QualityForge - 让AI系统持续自我优化*
