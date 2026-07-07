from benchmark.algorithms import DeutschAlgorithm
from benchmark.benchmark import BenchmarkRunner

algorithm = DeutschAlgorithm()

runner = BenchmarkRunner()

results = runner.run(algorithm)

print(results)