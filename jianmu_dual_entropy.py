"""
双熵互校
"""
import math
from collections import Counter


class DualEntropy:
    EPSILON = 1e-8
    DIRTY_THRESHOLD = 0.1

    def compute(self, text: str) -> dict:
        if not text or len(text.strip()) == 0:
            return {"status": "DIRTY", "confidence": 0.0, "reason": "空文本"}

        surface = self._surface_entropy(text)
        if surface < self.DIRTY_THRESHOLD:
            return {"status": "DIRTY", "confidence": 0.0, "reason": "表层熵过低"}

        structure = surface * 0.8
        gap = abs(surface - structure)
        confidence = max(0.0, 1 - gap / (surface + self.EPSILON))

        return {
            "status": "SUCCESS",
            "surface_entropy": round(surface, 6),
            "structure_entropy": round(structure, 6),
            "entropy_gap": round(gap, 6),
            "confidence": round(min(1.0, confidence), 6),
            "is_blocked": confidence < 0.5
        }

    def _surface_entropy(self, text: str) -> float:
        tokens = list(text)
        freq = Counter(tokens)
        total = len(tokens)
        ent = 0.0
        for cnt in freq.values():
            p = cnt / total
            ent -= p * math.log(p, 2)
        return ent