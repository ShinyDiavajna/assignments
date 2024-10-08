import numpy as np
import matplotlib.pyplot as plt

# Load data
points = np.loadtxt("points.dat", delimiter=',')
x_triangle = points[:60, 0]
y_triangle = points[:60, 1]
x_circle = points[60:, 0]
y_circle = points[60:, 1]

# Create the plot
plt.figure()
plt.plot(x_triangle, y_triangle, label='Triangle Edges')
plt.fill(x_triangle, y_triangle, 'lightblue', alpha=0.5)
plt.plot(x_circle, y_circle, label='Circle', color='orange')

# Define circle center
circle_center = (0, 0)

# Indicate the center with a point and annotate it
plt.plot(circle_center[0], circle_center[1], 'ro')  # Red point for the center
plt.annotate('O', xy=circle_center, xytext=(5, 5), textcoords='offset points', fontsize=12, color='red')

# Identify the topmost vertex of the triangle (assuming it's the first vertex in your data)
top_vertex = (x_triangle[0], y_triangle[0])

# Draw a line from the center to the top vertex
plt.plot([circle_center[0], top_vertex[0]], [circle_center[1], top_vertex[1]], 'k--')  # Dashed line
plt.annotate('2a', xy=((circle_center[0] + top_vertex[0]) / 2, (circle_center[1] + top_vertex[1]) / 2), 
                         fontsize=10, color='black')

# Plot settings
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Equilateral Triangle and Circle")
plt.grid(True)
plt.legend(loc="upper right")
plt.axis('equal')
plt.show()

