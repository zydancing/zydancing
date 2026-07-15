"""
建木·统一引擎
"""
from .time_lattice import TimeLattice
from .dual_entropy import DualEntropy
from .triple_road import TripleRoad
from .topology_sphere import TopologySphere
from .jellyfish_defense import JellyfishDefense
from .fan_brain import FanBrain
from .mobius_transport import MobiusTransport


class JianMuEngine:
    """建木统一入口"""

    def __init__(self):
        self.time_lattice = TimeLattice()
        self.dual_entropy = DualEntropy()
        self.triple_road = TripleRoad()
        self.topology_sphere = TopologySphere()
        self.jellyfish = JellyfishDefense()
        self.fan_brain = FanBrain()
        self.transport = MobiusTransport()

    def ping(self) -> str:
        return "建木·τ₀时序网格已激活"

    def run_dual_entropy(self, text: str) -> dict:
        return self.dual_entropy.compute(text)

    def run_triple_road(self, fact_id: str, model_id: str, data: dict) -> dict:
        return self.triple_road.validate(fact_id, model_id, data)

    def run_defense(self, request_id: str, text: str) -> dict:
        return self.jellyfish.process(request_id, text)

    def run_fan_brain(self, state, centers) -> dict:
        return self.fan_brain.evolve(state, centers)

    def run_transport(self, data, k_compress: float = 1.0) -> dict:
        return self.transport.transmit(data, k_compress)