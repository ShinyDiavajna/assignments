import matplotlib.pyplot as plt
import re

def read_points_from_file(filename):
    """Reads points from a text file and returns them as lists of x and y coordinates."""
    x_coords = []
    y_coords = []
    labels = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            line = line.strip()
            if line.startswith('Point'):
                # Extract coordinates using a regular expression
                match = re.search(r'\(([^,]+),\s*([^)]+)\)', line)
                if match:
                    try:
                        x = float(match.group(1).strip())
                        y = float(match.group(2).strip())
                        x_coords.append(x)
                        y_coords.append(y)
                        # Extract label for plotting
                        label = line.split(':')[0].strip()
                        labels.append(label)
                    except ValueError as e:
                        print(f"Warning: Could not convert to float. Error: {e}")
                else:
                    print(f"Warning: Could not find coordinates in line '{line}'")
    
    return x_coords, y_coords, labels

def plot_points(x_coords, y_coords, labels):
    """Plots the given x and y coordinates using matplotlib, including lines between points."""
    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords, color='red', label='Points')
    
    # Plot lines between points
    for i in range(len(x_coords) - 1):
        plt.plot([x_coords[i], x_coords[i + 1]], [y_coords[i], y_coords[i + 1]], 'b--', lw=2)

    # Labeling each point
    for x, y, label in zip(x_coords, y_coords, labels):
        plt.text(x, y, f'{label}', fontsize=12, ha='right')

    # Set labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plot of Points with Lines')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

def main():
    filename = 'plo1.txt'
    x_coords, y_coords, labels = read_points_from_file(filename)
    
    if not x_coords or not y_coords:
        print("No valid points to plot.")
    else:
        plot_points(x_coords, y_coords, labels)

if __name__ == '__main__':
    main()

