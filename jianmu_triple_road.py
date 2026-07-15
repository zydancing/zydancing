"""
三路校准：事实/逻辑/检索
"""
from typing import Dict, Any


class TripleRoad:
    THRESHOLD = 0.15

    def __init__(self):
        self.fact_archive = {}
        self.logic_model = {}
        self.conflict_log = []

    def load_fact(self, fact_id: str, fact_data: Dict):
        self.fact_archive[fact_id] = fact_data

    def load_logic(self, model_id: str, logic_func):
        self.logic_model[model_id] = logic_func

    def validate(self, fact_id: str, model_id: str, data: Dict) -> Dict:
        fact = self.fact_archive.get(fact_id)
        logic = self.logic_model.get(model_id)
        if fact is None or logic is None:
            return {"passed": False, "error": "fact or logic missing"}

        result = logic(data) if callable(logic) else logic
        fact_val = fact if isinstance(fact, (int, float)) else fact.get("value", 0.0)
        result_val = result if isinstance(result, (int, float)) else result.get("value", 0.0)

        deviation = abs(result_val - fact_val) / (abs(fact_val) + 1e-8)
        passed = deviation <= self.THRESHOLD

        if not passed:
            self.conflict_log.append({"fact_id": fact_id, "model_id": model_id, "deviation": deviation})

        return {"passed": passed, "deviation": round(deviation, 6), "threshold": self.THRESHOLD}

    def fuse_check(self) -> Dict:
        if len(self.conflict_log) > 0:
            return {"fuse_triggered": True, "conflicts": self.conflict_log}
        return {"fuse_triggered": False}