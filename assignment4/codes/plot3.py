import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re

def read_points_from_file(filename):
    """Reads points from a text file and returns a list of tuples."""
    points = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Use regular expression to find coordinates in the format (x, y, z)
                match = re.search(r'\(([-\d.]+),\s*([-\d.]+),\s*([-\d.]+)\)', line)
                if match:
                    x, y, z = map(float, match.groups())
                    points.append((x, y, z))
                else:
                    print(f"Warning: Line '{line.strip()}' is not in the correct format.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    return points

def plot_points(points):
    """Plots lines between points and labels them in a 3D plot."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if points:
        # Unzip the points into x, y, z coordinates
        x_coords, y_coords, z_coords = zip(*points)
        
        # Plot lines between points
        ax.plot(x_coords, y_coords, z_coords, marker='o', linestyle='-')

        # Define labels
        labels = ['A', 'B', 'C']

        # Annotate points
        for label, (x, y, z) in zip(labels, points):
            ax.text(x, y, z, f'{label} ({x:.1f}, {y:.1f}, {z:.1f})', fontsize=12, ha='right')

        ax.set_xlabel('$X axis$')
        ax.set_ylabel('$Y axis$')
        ax.set_zlabel('$Z axis$')

        # Remove plot title
        plt.show()
    else:
        print("No points to plot.")

def main():
    filename = 'plot3.txt'
    points = read_points_from_file(filename)
    if len(points) != 3:
        print(f"Warning: Expected 3 points, but found {len(points)} points.")
    plot_points(points)

if __name__ == "__main__":
    main()

