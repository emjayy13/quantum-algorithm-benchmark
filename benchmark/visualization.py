from pathlib import Path

import csv
import matplotlib.pyplot as plt


class BenchmarkVisualizer:
    """
    Creates benchmark comparison plots.
    """

    def __init__(
        self,
        csv_file="results/csv/benchmark_results.csv",
        output_dir="results/plots",
    ):

        self.csv_file = Path(csv_file)
        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def load_data(self):
        """
        Load benchmark results from the CSV file.
        """

        if not self.csv_file.exists():
            raise FileNotFoundError(
                f"Benchmark file not found: {self.csv_file}"
            )

        with open(self.csv_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    
    def plot_runtime(self):
        self._plot_metric(
            metric="runtime_seconds",
            title="Runtime Comparison",
            ylabel="Runtime (seconds)",
            filename="runtime_comparison.png",
        )

    def _plot_metric(
        self,
        metric: str,
        title: str,
        ylabel: str,
        filename: str,
    ):
        """
        Generic function to plot any benchmark metric.
        """

        data = self.load_data()
        algorithms = [row["algorithm"] for row in data]
        values = [float(row[metric]) for row in data]
        plt.figure(figsize=(8, 5))
        bars = plt.bar(algorithms, values)
        plt.title(title)
        plt.xlabel("Algorithm")
        plt.ylabel(ylabel)

        # Show the value above each bar
        for bar in bars:
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f"{height:.2f}",
                ha="center",
                va="bottom",
                fontsize=9,
            )

        plt.xticks(rotation=15)
        plt.tight_layout()
        output_file = self.output_dir / filename
        plt.savefig(output_file, dpi=300)
        plt.close()
        print(f"Saved: {output_file}")

    def plot_depth(self):
        self._plot_metric(
            metric="depth",
            title="Circuit Depth Comparison",
            ylabel="Circuit Depth",
            filename="depth_comparison.png",
        )
    
    def plot_gate_count(self):
        self._plot_metric(
            metric="gate_count",
            title="Gate Count Comparison",
            ylabel="Gate Count",
            filename="gate_count_comparison.png",
        )