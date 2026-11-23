# cpu_bound

CPU-bound matrix operations benchmark comparing **sequential** and **multithreaded** execution in Python.

## Overview

`cpu_bound` is a benchmark designed to explore CPU-bound performance in Python. It compares single-threaded against multi-threaded execution across matrix addition, multiplication, and transposition to analyze Python's Global Interpreter Lock (GIL) and concurrency overhead.

## Features

- **Execution Modes**: Seamless switching between sequential and multithreaded (`ThreadPoolExecutor`) runs.
- **Matrix Operations**: Addition ($O(N^2)$), Multiplication ($O(N^3)$), and Transposition.
- **Customizable Dimensions**: Run benchmarks across arbitrary row and column sizes.
- **Random Data Generation**: Toggle between zero-filled and floating-point random matrices (`[0.0, 1.0)`).
- **Strategy Architecture**: Built on an extensible `MatrixBase` abstract class following clean OOP design.

## Requirements

- Python 3.10+
- Standard library only (`argparse`, `concurrent.futures`, `time`, `random`, `typing`, `abc`)

## Usage

```bash
python3 cpu_bench.py [options]
```

### Options

| Flag | Long Flag | Description | Default |
| :--- | :--- | :--- | :--- |
| `-r` | `--rows` | Number of rows (required) | — |
| `-c` | `--cols` | Number of columns (required) | — |
| `-o` | `--op` | Operation: `add`, `mult`, `transpose` | `add` |
| `-m` | `--mode` | Execution mode: `sequential`, `threaded` | `sequential` |
| | `--random` | Fill matrices with random floats instead of zeros | `False` |
| `-h` | `--help` | Show usage information | — |

## Examples

### Matrix Addition Benchmark

```bash
# Sequential addition
python3 cpu_bench.py -r 1000 -c 1000 --random -m sequential -o add

# Multithreaded addition
python3 cpu_bench.py -r 1000 -c 1000 --random -m threaded -o add
```

### Matrix Multiplication Benchmark

```bash
# Sequential multiplication
python3 cpu_bench.py -r 300 -c 300 --random -m sequential -o mult

# Multithreaded multiplication
python3 cpu_bench.py -r 300 -c 300 --random -m threaded -o mult
```

## Performance & Benchmarks

Sample execution on an 8-core CPU (Python 3.14):

| Operation | Size | Mode | Elapsed Time | Note |
| :--- | :--- | :--- | :--- | :--- |
| Addition | $500 \times 500$ | Sequential | ~0.009s | Baseline |
| Addition | $500 \times 500$ | Threaded | ~0.018s | Thread overhead dominates |
| Multiplication | $300 \times 300$ | Sequential | ~1.13s | Baseline |
| Multiplication | $300 \times 300$ | Threaded | ~0.71s | ~1.6x speedup (GIL constrained) |

> [!NOTE]
> In standard CPython, pure Python CPU-bound workloads are constrained by the **Global Interpreter Lock (GIL)**, preventing full linear multi-core scaling with threads.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
