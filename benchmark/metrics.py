from typing import Any

from qiskit import QuantumCircuit


class MetricsCollector:
    """
    Collects benchmark metrics from a quantum circuit execution.
    """

    @staticmethod
    def collect(
        original_circuit: QuantumCircuit,
        transpiled_circuit: QuantumCircuit,
        runtime: float,
        counts: dict[str, int],
    ) -> dict[str, Any]:
        """
        Return benchmark metrics for a circuit.
        """

        return {
            "depth": original_circuit.depth(),
            "gate_count": original_circuit.size(),
            "operation_counts": dict(original_circuit.count_ops()),
            "transpiled_operation_counts": dict(transpiled_circuit.count_ops()),
            "transpiled_depth": transpiled_circuit.depth(),
            "transpiled_gate_count" : sum(transpiled_circuit.count_ops().values()),
            "num_qubits": original_circuit.num_qubits,
            "runtime_seconds": runtime,
            "counts": counts,
        }