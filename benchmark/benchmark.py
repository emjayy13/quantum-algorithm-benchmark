import time 
from typing import Any
from qiskit_aer import AerSimulator
from benchmark.algorithms import QuantumAlgorithm

DEFAULT_SHOTS= 1024

class BenchmarkRunner:
    """Runs quantum algorithms and collects benchmark metrics"""

    def __init__(self, shots:int=DEFAULT_SHOTS):
        self.backend= AerSimulator()
        self.shots= shots
    
    def run(self, algorithm: QuantumAlgorithm) -> dict[str,Any]:
        """Execute a quantum algorithm and return benchmark results"""

        circuit= algorithm.build_circuit()
        start_time= time.perf_counter()
        job= self.backend.run(circuit,shots=self.shots)
        result= job.result()

        runtime=time.perf_counter() - start_time
        counts= result.get_counts()

        return{
            "algorithm" : algorithm.name,
            "qubits" : algorithm.num_qubits,
            "depth" : circuit.depth(),
            "gate_count" : circuit.size(),
            "runtime_seconds": runtime,
            "shots": self.shots,
            "counts": counts,
        }
    