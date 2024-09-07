import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_points(filename):
    points = {}
    with open(filename, 'r') as file:
        for line in file:
            if 'Point P:' in line:
                match = re.search(r"Point P: \(([^,]+), ([^,]+), ([^)]*)\)", line)
                if match:
                    points['P'] = tuple(map(float, match.groups()))
            elif 'Q1:' in line:
                match = re.search(r"Q1: \(0, ([^,]+), 0\)", line)
                if match:
                    points['Q1'] = (0, float(match.group(1)), 0)
            elif 'Q2:' in line:
                match = re.search(r"Q2: \(0, ([^,]+), 0\)", line)
                if match:
                    points['Q2'] = (0, float(match.group(1)), 0)
    return points

def plot_points(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Extract coordinates
    labels = []
    xs, ys, zs = [], [], []
    for label, (x, y, z) in points.items():
        xs.append(x)
        ys.append(y)
        zs.append(z)
        ax.scatter(x, y, z, s=100, label=label)
        ax.text(x, y, z, f'{label}\n({x:.2f}, {y:.2f}, {z:.2f})', fontsize=12)

    # Draw lines between points, but exclude the line between Q2 and P
    point_names = list(points.keys())
    for i in range(len(point_names)):
        for j in range(i + 1, len(point_names)):
            if not (point_names[i] == 'Q2' and point_names[j] == 'P') and not (point_names[i] == 'P' and point_names[j] == 'Q2'):
                x1, y1, z1 = points[point_names[i]]
                x2, y2, z2 = points[point_names[j]]
                ax.plot([x1, x2], [y1, y2], [z1, z2], 'k--', lw=1)

    # Set labels and title
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    ax.legend()

    plt.show()

if __name__ == "__main__":
    points = read_points("plot.txt")
    plot_points(points)

