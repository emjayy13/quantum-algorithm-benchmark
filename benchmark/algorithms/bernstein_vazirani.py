from qiskit import QuantumCircuit
from benchmark.algorithms.base import QuantumAlgorithm

class BernsteinVaziraniAlgorithm(QuantumAlgorithm):
    """
    Implementation of the Bernstein-Vazirani Algorithm.
    """
    
    def __init__(self, secret: str):
        if not all(bit in "01" for bit in secret):
            raise ValueError(
                "Secret must contain only 0 and 1."
            )

        super().__init__(
            "Bernstein-Vazirani",
            len(secret) + 1
        )

        self.secret = secret

    def build_circuit(self) -> QuantumCircuit:

        n = len(self.secret)

        qc = QuantumCircuit(n + 1, n)

        qc.x(n)

        qc.h(range(n + 1))

        for i, bit in enumerate(self.secret):
            if bit == "1":
                qc.cx(i, n)

        qc.h(range(n))

        qc.measure(range(n), range(n))

        return qc