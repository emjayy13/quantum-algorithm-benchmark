import time 
from typing import Any
from qiskit_aer import AerSimulator
from benchmark.algorithms import QuantumAlgorithm
from benchmark.metrics import MetricsCollector
from benchmark.exporter import CSVExporter
from qiskit import transpile

DEFAULT_SHOTS= 1024

class BenchmarkRunner:
    """Runs quantum algorithms and collects benchmark metrics"""

    def __init__(self, shots:int=DEFAULT_SHOTS):
        self.backend= AerSimulator()
        self.shots= shots
        self.exporter = CSVExporter()
    
    def run(self, algorithm: QuantumAlgorithm) -> dict[str,Any]:
        """Execute a quantum algorithm and return benchmark results"""

        circuit= algorithm.build_circuit()
        transpiled_circuit= transpile(circuit, backend= self.backend, optimization_level=3,)
        start_time= time.perf_counter()
        job= self.backend.run(transpiled_circuit,shots=self.shots,)
        result= job.result()

        runtime=time.perf_counter() - start_time
        counts= result.get_counts()

        metrics = MetricsCollector.collect(
                    original_circuit=circuit,
                    transpiled_circuit=transpiled_circuit,
                    runtime=runtime,
                    counts=counts,
        )

        result = {
                "algorithm": algorithm.name,
                **metrics,
                "shots": self.shots,
            }

        self.exporter.export(result)

        return result
    