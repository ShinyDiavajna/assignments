#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function declarations
double **createMat(int m, int n);
void writeCircleToFile(double center[], double radius);

int main() {
    // Center of the circle
    double center[2] = {0.0, 0.0}; // Center at origin (0, 0)
    
    // Radius of the circle
    double radius = 2.0; // 2a, assuming a=1 for simplicity
    
    // Write center and radius to a file
    writeCircleToFile(center, radius);

    return 0;
}

void writeCircleToFile(double center[], double radius) {
    FILE *fp = fopen("plot.txt", "w");
    if (fp == NULL) {
        fprintf(stderr, "Error opening file!\n");
        exit(1);
    }

    fprintf(fp, "Center of Circle: (%.2f, %.2f)\n", center[0], center[1]);
    fprintf(fp, "Radius of Circle: %.2f\n", radius);
    fprintf(fp, "Note: The value of 'a' is considered as 1.\n"); // Mentioning the value of 'a'
    fclose(fp);
}

// Define createMat if needed
double **createMat(int m, int n) {
    int i;
    double **a;
    
    // Allocate memory to the pointer
    a = (double **)malloc(m * sizeof(*a));
    for (i = 0; i < m; i++)
        a[i] = (double *)malloc(n * sizeof(*a[i]));

    return a;
}

