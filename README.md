# greenwich-conduction

Finite difference heat conduction optimization problem

# getting started

Requirements

-   Linux (Ubuntu).
-   VS Code (with CPP extension).
-   C++ compiler (`sudo apt install g++`).

Compile the source with,

```sh
g++ -o build/gauss src/gauss.cpp
```

Run the code with,

```sh
build/gauss 5 5 0.01 # m, n, tol
#> build/gauss 5 5 0.01
#> :
```

Run and store output,

```sh
build/gauss 5 5 0.01 > results/gauss/output.txt
```

# results

Runtime and results plots are managed in Python,

```py
# app.py

import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt

method = "jacobi2d"

```

The [outputs](results/gauss/output.txt), [runtimes](results/gauss/execution_time.txt), and [plots](results/plots/).