from benchmark.algorithms import GroverAlgorithm
from benchmark.benchmark import BenchmarkRunner
algorithm = GroverAlgorithm()
runner = BenchmarkRunner()
result = runner.run(algorithm)
print(result)