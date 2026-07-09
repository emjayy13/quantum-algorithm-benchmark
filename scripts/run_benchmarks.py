from benchmark.algorithms import (
    DeutschAlgorithm,
    BernsteinVaziraniAlgorithm,
    GroverAlgorithm,
    QFTAlgorithm,
)
from benchmark.export import CSVExporter
from benchmark.benchmark import BenchmarkRunner
from benchmark.visualization import BenchmarkVisualizer

runner = BenchmarkRunner()
exporter = CSVExporter()

algorithms = [
    DeutschAlgorithm(),
    BernsteinVaziraniAlgorithm("1101"),
    GroverAlgorithm(),
    QFTAlgorithm(),
]

from pathlib import Path
csv_file = Path("results/csv/benchmark_results.csv")
if csv_file.exists():
    csv_file.unlink()

for algorithm in algorithms:
    print(f"Running {algorithm.name}...")
    result = runner.run(algorithm)
    exporter.save(result)
    print("Done ✓")