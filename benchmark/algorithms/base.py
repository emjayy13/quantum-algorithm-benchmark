from abc import ABC, abstractmethod
from qiskit import QuantumCircuit

class QuantumAlgorithm(ABC):
    """
    Base class for all quantum algorithm in the benchmarking framework.
    """
    def __init__(self, name:str, num_qubits: int):
        self.name=name
        self.num_qubits= num_qubits

    @abstractmethod
    def build_circuit(self)-> QuantumCircuit:
        """Build and return the quantum circuit."""

        pass
