from benchmark.algorithms import QFTAlgorithm
from benchmark.benchmark import BenchmarkRunner

algorithm = QFTAlgorithm(3)
runner = BenchmarkRunner()
result = runner.run(algorithm)
print(result)