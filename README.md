# cpu_bound

CPU-bound matrix operations benchmark comparing **sequential**, **multithreaded**, and **multiprocessing** execution in Python.

## Overview

`cpu_bound` is a benchmark designed to explore CPU-bound performance in Python. It compares single-threaded, multi-threaded, and multi-process execution across matrix addition, multiplication, and transposition to analyze Python's Global Interpreter Lock (GIL), process serialization overhead, and multi-core scaling.

## Requirements

- Python 3.10+
- Standard library only (`argparse`, `concurrent.futures`, `time`, `random`, `typing`, `abc`, `logging`)

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
| `-m` | `--mode` | Execution mode: `sequential`, `threaded`, `parallel` | `sequential` |
| | `--random` | Fill matrices with random floats instead of zeros | `False` |
| `-h` | `--help` | Show usage information | — |

## Execution Modes

| Mode | Implementation | CPU Cores Used | Behavior on CPU-Bound Tasks |
| :--- | :--- | :--- | :--- |
| **`sequential`** | Single thread | 1 Core | Baseline single-core execution. |
| **`threaded`** | `ThreadPoolExecutor` | 1 Core (at a time) | Constrained by the **GIL**. Bytecode is serialized; switching overhead makes it equal to or slower than sequential. |
| **`parallel`** | `ProcessPoolExecutor` | All Available Cores | Bypasses the GIL by spawning worker processes with independent interpreters. Delivers true multi-core speedup for compute-heavy tasks. |

## Examples

### Matrix Multiplication Benchmark ($O(N^3)$ — Compute Heavy)

```bash
# Sequential multiplication (baseline)
python3 cpu_bench.py -r 500 -c 500 --random -m sequential -o mult

# Multithreaded multiplication (GIL-bound)
python3 cpu_bench.py -r 500 -c 500 --random -m threaded -o mult

# Multiprocessing multiplication (True multi-core parallelism)
python3 cpu_bench.py -r 500 -c 500 --random -m parallel -o mult
```

### Matrix Addition Benchmark ($O(N^2)$ — Memory / IPC Bound)

```bash
# Sequential addition
python3 cpu_bench.py -r 2000 -c 2000 --random -m sequential -o add

# Multithreaded addition
python3 cpu_bench.py -r 2000 -c 2000 --random -m threaded -o add

# Multiprocessing addition
python3 cpu_bench.py -r 2000 -c 2000 --random -m parallel -o add
```

> [!NOTE]
> - **Matrix Multiplication (`mult`)**: Heavy computation heavily outweighs inter-process communication (IPC) costs, so `-m parallel` yields significant speedups.
> - **Matrix Addition (`add`)**: The computation is lightweight ($O(N^2)$), meaning the overhead of serializing (pickling) large matrices between worker processes can make `parallel` slower than `sequential`.
> - **Threads and the GIL**: In standard CPython, `-m threaded` cannot run pure Python bytecode simultaneously on multiple cores due to the Global Interpreter Lock.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
