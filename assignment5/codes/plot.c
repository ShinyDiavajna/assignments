#include <stdio.h>
#include <math.h>

int main() {
    // Define the point P
    double x1, y1, z1;
    double distance = 5 * sqrt(2);  // Distance to Q

    // Input point P coordinates
    x1=3;
    y1=-2;
    z1=5;

    // Calculate the y-coordinate of point Q
    double rhs = distance * distance; // (5*sqrt(2))^2 = 50
    double x1_squared = x1 * x1;
    double z1_squared = z1 * z1;
    double y_diff_squared = rhs - x1_squared - z1_squared;

    if (y_diff_squared < 0) {
        printf("No real solution exists.\n");
        return 1;
    }

    // Two possible solutions for y
    double y_positive = y1 + sqrt(y_diff_squared);
    double y_negative = y1 - sqrt(y_diff_squared);

    // Print results to plot.txt
    FILE *file = fopen("plot.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "Point P: (%.2f, %.2f, %.2f)\n", x1, y1, z1);
    fprintf(file, "Q1: (0, %.2f, 0)\n", y_positive);
    fprintf(file, "Q2: (0, %.2f, 0)\n", y_negative);

    fclose(file);

    return 0;
}

