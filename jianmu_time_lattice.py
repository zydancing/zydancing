"""
时序网格·光速修正与精细结构常数
"""
import math


class TimeLattice:
    PHI = (5 ** 0.5 - 1) / 2
    TAU_DENSITY_BASE = 3.21e-19
    ELASTIC_COMP = 0.9999
    PLANCK_SCALE = 1e35
    GAMMA_SCALE = 1e36
    C0 = 299792458.0

    @classmethod
    def light_speed_correction(cls, k_compress: float) -> dict:
        rho_tau = k_compress * cls.TAU_DENSITY_BASE
        beta = cls.ELASTIC_COMP / cls.PLANCK_SCALE
        gamma = (cls.PHI ** 2) * math.log(1.0 / cls.PHI) * cls.GAMMA_SCALE
        v_local = cls.C0 * (1 - beta * rho_tau + gamma * rho_tau ** 2)
        return {
            "local_speed": v_local,
            "c_ratio": v_local / cls.C0,
            "offset": 1 - v_local / cls.C0
        }

    @classmethod
    def fine_structure(cls) -> dict:
        ideal = 3 ** 0.5 / 2
        k_bottom = 0.2875
        P = 2.751
        alpha = 1.0 / (100 * ideal * k_bottom * P * 2)
        return {"alpha": alpha, "alpha_inv": 1.0 / alpha}