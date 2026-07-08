from benchmark.algorithms import BernsteinVaziraniAlgorithm
from benchmark.benchmark import BenchmarkRunner

algorithm = BernsteinVaziraniAlgorithm("1011")

runner = BenchmarkRunner()

result = runner.run(algorithm)

print(result)