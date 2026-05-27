# QualityForge - Self-Improving AI Quality System
# Auto-score, auto-regenerate, auto-learn

from typing import Callable, Optional

class QualityScorer:
    """
    Multi-dimensional quality scoring for AI outputs.
    
    Dimensions:
    - Accuracy: Factual correctness
    - Relevance: Alignment with query
    - Coherence: Logical consistency
    - Completeness: Coverage of topic
    """

    def __init__(self):
        self.thresholds = {
            "accuracy": 0.75,
            "relevance": 0.70,
            "coherence": 0.80,
            "completeness": 0.65
        }
        self.history = []

    def score(self, output: str, query: str = "", expected: str = "") -> dict:
        """Score output across all dimensions."""
        scores = {
            "accuracy": self._score_accuracy(output),
            "relevance": self._score_relevance(output, query),
            "coherence": self._score_coherence(output),
            "completeness": self._score_completeness(output)
        }
        overall = sum(scores.values()) / len(scores)
        result = {
            "scores": scores,
            "overall": overall,
            "passed": all(scores[k] >= self.thresholds[k] for k in self.thresholds),
            "weakest_dimension": min(scores, key=scores.get)
        }
        self.history.append(result)
        return result

    def _score_accuracy(self, output: str) -> float:
        # Simplified: check for known false patterns
        false_indicators = ["always wrong", "proven false"]
        if any(ind in output.lower() for ind in false_indicators):
            return 0.3
        return 0.85

    def _score_relevance(self, output: str, query: str) -> float:
        if not query:
            return 0.8
        query_words = set(query.lower().split())
        output_words = set(output.lower().split())
        overlap = len(query_words & output_words) / max(len(query_words), 1)
        return min(overlap + 0.5, 1.0)

    def _score_coherence(self, output: str) -> float:
        sentences = output.split(".")
        if len(sentences) < 2:
            return 0.7
        return 0.9

    def _score_completeness(self, output: str) -> float:
        length = len(output)
        if length < 100:
            return 0.4
        if length < 300:
            return 0.7
        return 0.9


class AutoRegenerator:
    """Automatically regenerate outputs that fail quality checks."""

    def __init__(self, scorer: QualityScorer, generator: Callable):
        self.scorer = scorer
        self.generator = generator
        self.max_attempts = 3

    def generate(self, query: str, context: str = "") -> dict:
        """Generate with auto-regeneration on failure."""
        attempts = []
        for i in range(self.max_attempts):
            output = self.generator(query, context)
            result = self.scorer.score(output, query)
            result["attempt"] = i + 1
            attempts.append(result)
            if result["passed"]:
                result["final"] = True
                return result
        return {
            "passed": False,
            "attempts": attempts,
            "final": False,
            "best_score": max(a["overall"] for a in attempts)
        }


class LearningEngine:
    """Learn from quality scores to improve future outputs."""

    def __init__(self):
        self.patterns = {}

    def learn(self, query: str, scores: dict):
        """Record pattern for similar future queries."""
        words = query.lower().split()
        for word in words:
            if word not in self.patterns:
                self.patterns[word] = []
            self.patterns[word].append(scores["overall"])

    def get_insight(self, query: str) -> Optional[float]:
        """Get average score for similar queries."""
        words = query.lower().split()
        all_scores = []
        for word in words:
            if word in self.patterns:
                all_scores.extend(self.patterns[word])
        return sum(all_scores) / len(all_scores) if all_scores else None


if __name__ == "__main__":
    scorer = QualityScorer()
    result = scorer.score("AI models improve with scale. This has been proven.", "AI development")
    print("Quality:", result)