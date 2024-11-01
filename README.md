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

# plot results

