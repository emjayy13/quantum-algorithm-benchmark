from pathlib import Path
import csv


class CSVExporter:
    """
    Saves benchmark results to a CSV file.
    """

    def __init__(self, filename="results/csv/benchmark_results.csv"):
        self.filename = Path(filename)
        self.filename.parent.mkdir(parents=True, exist_ok=True)

    def save(self, result: dict):
        file_exists = self.filename.exists()

        with open(self.filename, "a", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=result.keys(),
            )

            if not file_exists:
                writer.writeheader()

            writer.writerow(result)