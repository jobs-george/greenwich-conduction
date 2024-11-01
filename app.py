# app.py

import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt

method = "gauss"  # gauss
flag_compile = False

# Compile the C++ code (only needed once or if code changes)
if flag_compile:
    compile_process = subprocess.run(["g++", "-o", f"build/{method}", f"src/{method}.cpp"])
    if compile_process.returncode != 0:
        print("Compilation failed!")
        exit(1)

# Run the C++ executable and measure its runtime
m, n, tol = 1000, 1000, 0.01  # Set your parameters here
start_time = time.time()  # Start timer

with open(f"results/{method}/output.txt", "w") as output_file:
    run_process = subprocess.run(
        [f"build/{method}", str(m), str(n), str(tol)], stdout=output_file
    )

# Check if the C++ executable ran successfully
if run_process.returncode != 0:
    print("Execution failed!")
    exit(1)

end_time = time.time()  # End timer
runtime = end_time - start_time
print(f"Execution time: {runtime:.4f} seconds")

# Write execution time to a file
with open(f"results/{method}/execution_time.txt", "w") as file:
    file.write(f"Execution time: {runtime:.4f} seconds\n")

# Read data from the output file
data = []
with open(f"results/{method}/output.txt", "r") as file:
    lines = file.readlines()

    # Skip the first line with iteration info
    for line in lines[3:]:
        row = list(map(float, line.strip().split()))
        data.append(row)

# Convert data to a NumPy array
data = np.array(data)

# Plot the temperature grid
plt.figure(figsize=(8, 6))
plt.imshow(data, cmap="hot", interpolation="nearest")
plt.colorbar(label="Temperature")
plt.title(f"Temperature Distribution ({method})")
plt.xlabel("Grid Column")
plt.ylabel("Grid Row")

# Save the plot to a file
plt.savefig(
    f"results/plots/temperature_distribution_{method}.png", dpi=300, bbox_inches="tight"
)

# Optionally, display the plot
plt.show()
