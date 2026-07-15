"""
四维拓扑离散球
"""
import math


class TopologySphere:
    def __init__(self, threshold_strict=15.0, threshold_divergent=30.0):
        self.threshold_strict = threshold_strict
        self.threshold_divergent = threshold_divergent

    def map_to_sphere(self, content: str) -> tuple:
        h = hash(content)
        x = (h & 0xFF) / 255.0 * 2 - 1
        y = ((h >> 8) & 0xFF) / 255.0 * 2 - 1
        z = ((h >> 16) & 0xFF) / 255.0 * 2 - 1
        norm = math.sqrt(x ** 2 + y ** 2 + z ** 2)
        if norm < 1e-8:
            return (0.0, 0.0, 0.0)
        return (x / norm, y / norm, z / norm)

    def compute_curvature(self, pos1: tuple, pos2: tuple) -> float:
        dot = pos1[0] * pos2[0] + pos1[1] * pos2[1] + pos1[2] * pos2[2]
        dot = max(-1.0, min(1.0, dot))
        return math.degrees(math.acos(dot))

    def classify(self, curvature: float) -> str:
        if curvature <= self.threshold_strict:
            return "normal"
        elif curvature <= self.threshold_divergent:
            return "divergent"
        return "break"