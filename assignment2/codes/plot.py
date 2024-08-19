import matplotlib.pyplot as plt

# Define the coordinates of the points
x = [4, 8, 2]
y = [2, 4, 1]

# Define the names for each point
names = ['A', 'B', 'P']

# Create a scatter plot
plt.scatter(x, y, color='green', marker='o', s=100)

# Connect the points with lines
plt.plot(x, y, color='blue', linestyle='-', linewidth=1.5)  # Line connecting the points

# Annotate each point with its name
for i, name in enumerate(names):
    plt.annotate(name, (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Add title and labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show grid
plt.grid(True)

# Show the plot
plt.show()

