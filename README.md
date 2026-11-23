# cpu_bound

CPU-bound matrix operations benchmark comparing **sequential** and **multithreaded** execution in Python.

## Overview

`cpu_bound` is a benchmark designed to explore CPU-bound performance in Python. It compares single-threaded against multi-threaded execution across matrix addition, multiplication, and transposition to analyze Python's Global Interpreter Lock (GIL) and concurrency overhead.

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

> [!NOTE]
> In standard CPython, pure Python CPU-bound workloads are constrained by the **Global Interpreter Lock (GIL)**, preventing full linear multi-core scaling with threads.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
