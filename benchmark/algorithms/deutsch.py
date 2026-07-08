from qiskit import QuantumCircuit
from benchmark.algorithms.base import QuantumAlgorithm

class DeutschAlgorithm(QuantumAlgorithm):
    """Implementation of the Deutsch Algorithm"""

    def __init__(self):
        super().__init__("Deutsch",2)
    def build_circuit(self) -> QuantumCircuit:
        qc= QuantumCircuit(2,1)

        #prepare the second qubit in |1>
        qc.x(1)

        #apply hadamard gate
        qc.h([0,1])

        #oracle (constant function example)
        qc.h(0)

        qc.measure(0,0)
        return qc