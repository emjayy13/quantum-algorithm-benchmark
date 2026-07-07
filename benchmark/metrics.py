from typing import Any

from qiskit import QuantumCircuit


class MetricsCollector:
    """
    Collects benchmark metrics from a quantum circuit execution.
    """

    @staticmethod
    def collect(
        circuit: QuantumCircuit,
        runtime: float,
        counts: dict[str, int],
    ) -> dict[str, Any]:
        """
        Return benchmark metrics for a circuit.
        """

        return {
            "depth": circuit.depth(),
            "gate_count": circuit.size(),
            "num_qubits": circuit.num_qubits,
            "runtime_seconds": runtime,
            "counts": counts,
        }