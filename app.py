import numpy as np
import matplotlib.pyplot as plt

# Read data from the output file
data = []
with open("results/gauss/output.txt", "r") as file:
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
plt.title("Temperature Distribution")
plt.xlabel("Grid Column")
plt.ylabel("Grid Row")

# Save the plot to a file
plt.savefig("results/plots/temperature_distribution.png", dpi=300, bbox_inches="tight")

# Optionally, display the plot
plt.show()
