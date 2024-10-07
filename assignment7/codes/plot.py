import matplotlib.pyplot as plt
import numpy as np

def read_circle_parameters(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Extract center coordinates
        center_line = lines[0].strip().split(': ')[1].strip('()').split(', ')
        center = (float(center_line[0]), float(center_line[1]))
        
        # Extract radius
        radius_line = lines[1].strip().split(': ')[1]
        radius = float(radius_line)
    
    return center, radius

def plot_circle_and_triangle(center, radius):
    fig, ax = plt.subplots()
    
    # Create a circle (circumcircle)
    circle = plt.Circle(center, radius, color='blue', fill=False, linewidth=2)
    ax.add_artist(circle)
    
    # Calculate side length of the triangle based on the circumradius
    a = radius * np.sqrt(3)  # Side length of the equilateral triangle

    # Vertices of the equilateral triangle
    vertices = np.array([
        [center[0] - a / 2, center[1] - radius / 2],
        [center[0] + a / 2, center[1] - radius / 2],
        [center[0], center[1] + radius]
    ])

    # Draw the triangle
    triangle = plt.Polygon(vertices, color='orange', fill=None, linewidth=2)
    ax.add_artist(triangle)

    # Draw a dot at the center and label it O
    ax.plot(center[0], center[1], 'ro')  # Red dot at center
    ax.annotate('O', xy=center, xytext=(center[0] + 0.1, center[1] + 0.1),
                fontsize=12, ha='center', color='black', weight='bold')
    
    # Set limits and aspect
    ax.set_xlim(center[0] - radius - 1, center[0] + radius + 1)
    ax.set_ylim(center[1] - radius - 1, center[1] + radius + 1)
    ax.set_aspect('equal', 'box')
    
    # Annotate radius with a line from center to a vertex
    radius_vertex = vertices[2]  # Using the top vertex of the triangle
    ax.plot([center[0], radius_vertex[0]], [center[1], radius_vertex[1]], 'k--')  # Dashed line
    ax.annotate('2a', xy=radius_vertex,
                xytext=(radius_vertex[0] + 0.1, radius_vertex[1] + 0.1),
                fontsize=12, ha='left', color='black', weight='bold')

    # Add grid and labels
    plt.grid()
    plt.xlabel('$X-axis$')
    plt.ylabel('$Y-axis$')
    
    # Show the plot
    plt.show()

# File path
file_path = 'plot.txt'

# Read the circle parameters
center, radius = read_circle_parameters(file_path)

# Plot the circle and triangle
plot_circle_and_triangle(center, radius)

