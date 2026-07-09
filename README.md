# Quantum Algorithm Benchmarking Framework

A modular benchmarking framework built with **Qiskit** to implement, execute, analyze, and compare fundamental quantum algorithms. The project provides a reusable architecture for benchmarking quantum circuits, collecting execution metrics, exporting benchmark results, and generating visual comparisons.

## Overview

Quantum algorithms are often compared based on theoretical complexity, but practical performance also depends on factors such as circuit depth, gate count, compiler optimizations, and execution characteristics. This framework provides a structured way to benchmark multiple quantum algorithms under a common interface and visualize their performance.

## Features

* Modular architecture using object-oriented design
* Common interface for implementing quantum algorithms
* Implementations of:

  * Deutsch Algorithm
  * Bernstein–Vazirani Algorithm
  * Grover's Search Algorithm
  * Quantum Fourier Transform (QFT)
* Automatic benchmarking pipeline
* Circuit metrics collection

  * Circuit depth
  * Gate count
  * Number of qubits
  * Runtime
  * Transpiled circuit depth
  * Transpiled gate count
  * Gate operation counts
* CSV export of benchmark results
* Automatic generation of comparison plots
* Clean, extensible project structure for adding new algorithms


## Architecture

The framework follows a modular architecture where each component has a single responsibility.

```text
                    +----------------------+
                    |  Quantum Algorithm   |
                    |   (Abstract Base)    |
                    +----------+-----------+
                               |
        +----------------------+----------------------+
        |                      |                      |
   Deutsch               Bernstein-Vazirani       Grover
                                                  |
                                                  |
                                                 QFT

                               |
                               ▼
                     BenchmarkRunner
                               |
             +-----------------+------------------+
             |                                    |
             ▼                                    ▼
      MetricsCollector                     AerSimulator
             |                                    |
             +-----------------+------------------+
                               |
                               ▼
                         Benchmark Results
                               |
                  +------------+-------------+
                  |                          |
                  ▼                          ▼
             CSV Exporter              Visualizer
```

### Component Responsibilities

| Component             | Responsibility                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------ |
| `QuantumAlgorithm`    | Defines the common interface for all quantum algorithms.                                   |
| `BenchmarkRunner`     | Executes algorithms and collects benchmark data.                                           |
| `MetricsCollector`    | Computes circuit metrics such as depth, gate count, runtime, and transpilation statistics. |
| `CSVExporter`         | Stores benchmark results in CSV format.                                                    |
| `BenchmarkVisualizer` | Generates comparison plots from benchmark data.                                            |

This design makes the framework easy to extend. New quantum algorithms can be added by implementing the `QuantumAlgorithm` interface without modifying the benchmarking pipeline.
