import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read points from points.txt
with open('points.txt', 'r') as file:
    points = [list(map(float, line.split(','))) for line in file]

# Separate the points into x, y, and z coordinates
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]
z_coords = [point[2] for point in points]

# Create a 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.plot(x_coords, y_coords, z_coords, 'o-', label='Points')

# Annotate points with labels and coordinates
labels = ['A', 'B', 'C']
for i, (x, y, z) in enumerate(zip(x_coords, y_coords, z_coords)):
    ax.text(x, y, z, f'{labels[i]} ({x}, {y}, {z})', size=10, zorder=1)


ax.set_xlabel('$X-axis$')
ax.set_ylabel('$Y-axis$')
ax.set_zlabel('$Z-axis$')
ax.grid(True)
ax.legend()

# Show the plot
plt.show()

