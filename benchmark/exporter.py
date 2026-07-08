import csv
from pathlib import Path


class CSVExporter:
    """
    Exports benchmark results to a CSV file.
    """

    def __init__(self, output_file: str = "results/csv/benchmark_results.csv"):
        self.output_file = Path(output_file)

        # Create parent directories if they don't exist
        self.output_file.parent.mkdir(parents=True, exist_ok=True)

    def export(self, result: dict):
        """
        Append a benchmark result to the CSV file.
        """

        file_exists = self.output_file.exists()

        with open(self.output_file, "a", newline="") as csvfile:

            writer = csv.DictWriter(
                csvfile,
                fieldnames=result.keys()
            )

            if not file_exists:
                writer.writeheader()

            writer.writerow(result)