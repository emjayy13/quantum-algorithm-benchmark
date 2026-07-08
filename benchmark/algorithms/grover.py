from qiskit import QuantumCircuit
from benchmark.algorithms.base import QuantumAlgorithm


class GroverAlgorithm(QuantumAlgorithm):
    """
    Implementation of Grover's Search Algorithm (2-qubit version).
    """

    def __init__(self):
        super().__init__("Grover", 2)

    def build_circuit(self) -> QuantumCircuit:
        qc = QuantumCircuit(2, 2)
        qc.h([0, 1])
        # Oracle
        qc.cz(0, 1)
        # Diffuser
        qc.h([0, 1])
        qc.x([0, 1])
        qc.h(1)
        qc.cx(0, 1)
        qc.h(1)
        qc.x([0, 1])
        qc.h([0, 1])
        qc.measure([0, 1], [0, 1])
        return qc   
        