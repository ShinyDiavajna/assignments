import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to read points from a file
def read_points(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            if 'Point' in line:
                parts = line.strip().split(': ')[1][1:-1]  # Extract the point coordinates
                x, y, z = map(float, parts.split(', '))
                points.append((x, y, z))
    return points

# Read the points from the file
filename = 'points.txt'
points = read_points(filename)

# Unpack points
x, y, z = zip(*points)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(x, y, z, color='r', s=100)  # s is the size of points

# Annotate points
for i, point in enumerate(points):
    ax.text(point[0], point[1], point[2], f'Point {i+1}', fontsize=12)

# Plot lines between the points
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        ax.plot([points[i][0], points[j][0]], 
                [points[i][1], points[j][1]], 
                [points[i][2], points[j][2]], 'b--')  # 'b--' for blue dashed lines

# Set labels
ax.set_xlabel($X$)
ax.set_ylabel($Y$)
ax.set_zlabel($Z$)

# Set title
ax.set_title('3D Plot of Points and Lines')

# Show plot
plt.show()

