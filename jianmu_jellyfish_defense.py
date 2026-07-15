"""
僧帽水母防御
"""
import time


class JellyfishDefense:
    DELAY_MAP = {0: 0, 1: 3000, 2: 5000, 3: 8000}

    def __init__(self):
        self.alert_log = []
        self.stats = {"total": 0, "bypass": 0, "delayed": 0}

    def process(self, request_id: str, text: str) -> dict:
        risk_level = self._assess_risk(text)
        self.stats["total"] += 1

        delay_ms = self.DELAY_MAP.get(risk_level, 0)
        if delay_ms == 0:
            self.stats["bypass"] += 1
            return {"request_id": request_id, "action": "bypass", "risk_level": risk_level, "delay_ms": 0}

        self.stats["delayed"] += 1
        time.sleep(delay_ms / 1000.0)

        return {"request_id": request_id, "action": "delayed", "risk_level": risk_level, "delay_ms": delay_ms}

    def _assess_risk(self, text: str) -> int:
        risk_keywords = ["攻击", "病毒", "入侵", "金融", "投资", "法律", "医疗"]
        for kw in risk_keywords:
            if kw in text:
                return 2
        if len(text) < 10:
            return 1
        return 0