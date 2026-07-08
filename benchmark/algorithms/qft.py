from math import pi
from qiskit import QuantumCircuit
from benchmark.algorithms.base import QuantumAlgorithm

class QFTAlgorithm(QuantumAlgorithm):
    """
    Quantum Fourier Transform.
    """

    def __init__(self, num_qubits: int = 3):
        super().__init__("Quantum Fourier Transform", num_qubits)
        
    
    def build_circuit(self):
        qc = QuantumCircuit(
            self.num_qubits,
            self.num_qubits
        )

        for target in range(self.num_qubits):
            qc.h(target)
            for control in range(target + 1, self.num_qubits):
                angle = pi / (2 ** (control - target))
                qc.cp(angle, control, target)

        #reverse the order
        for i in range(self.num_qubits // 2):
            qc.swap(i, self.num_qubits - i - 1)

        qc.measure(
        range(self.num_qubits),
        range(self.num_qubits)
        )

        return qc