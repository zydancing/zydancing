"""
折扇大脑：庞加莱双曲球 + 势能场
"""
import math


class FanBrain:
    DIM = 3
    EPS = 1e-12

    def evolve(self, state: list, centers: list, steps: int = 10) -> dict:
        """
        简化版演化：计算到最近中心的距离并判断收敛
        """
        if not state or not centers:
            return {"converged": False, "sector": -1, "final_state": state}

        final_state = state.copy()
        min_dist = float('inf')
        nearest = 0

        for i, c in enumerate(centers):
            dist = self._distance(state, c)
            if dist < min_dist:
                min_dist = dist
                nearest = i

        # 简单收敛判定：向中心移动
        for _ in range(steps):
            for i in range(self.DIM):
                final_state[i] += 0.1 * (centers[nearest][i] - final_state[i])

        return {
            "converged": min_dist < 0.3,
            "sector": nearest,
            "final_state": final_state,
            "distance_to_center": round(min_dist, 6)
        }

    def _distance(self, a: list, b: list) -> float:
        dot = sum(a[i] * b[i] for i in range(self.DIM))
        norm_a = math.sqrt(sum(x ** 2 for x in a))
        norm_b = math.sqrt(sum(y ** 2 for y in b))
        denom = 1.0 - dot
        denom = max(self.EPS, denom)
        r = (norm_a * norm_b) / denom
        r = min(0.99999, r)
        return math.acosh(1.0 + 2.0 * r ** 2 / (1.0 - r ** 2))