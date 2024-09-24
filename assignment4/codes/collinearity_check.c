#include <stdio.h>
#include <stdlib.h>
#include<math.h>
#include "matfun.h"

// Function to calculate the rank of a matrix using row reduction
int rank(double **m, int rows, int cols) {
    double **temp = createMat(rows, cols);
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            temp[i][j] = m[i][j];

    int rank = cols; // Start with max rank
    for (int r = 0; r < rank; r++) {
        // Check if the leading entry is zero
        if (temp[r][r] == 0) {
            // Find a non-zero element in the current column
            for (int i = r + 1; i < rows; i++) {
                if (temp[i][r] != 0) {
                    // Swap rows
                    for (int j = 0; j < cols; j++) {
                        double t = temp[r][j];
                        temp[r][j] = temp[i][j];
                        temp[i][j] = t;
                    }
                    break;
                }
            }
        }
        // If the leading entry is still zero, reduce rank
        if (temp[r][r] == 0) {
            rank--;
            for (int i = 0; i < rows; i++) {
                temp[i][r] = temp[i][rank];
            }
        }
        // Make all entries below the leading entry zero
        for (int i = r + 1; i < rows; i++) {
            double factor = temp[i][r] / temp[r][r];
            for (int j = r; j < cols; j++)
                temp[i][j] -= factor * temp[r][j];
        }
    }
    // Free the temporary matrix
    for (int i = 0; i < rows; i++)
        free(temp[i]);
    free(temp);
    return rank;
}

int main() {
    // Points as vectors
    double **M = createMat(3, 2);
    
    // Load points from file
    FILE *file = fopen("points.txt", "r");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    double x1, y1, z1;
    double x2, y2, z2;
    double x3, y3, z3;

    fscanf(file, "%lf %lf %lf", &x1, &y1, &z1);
    fscanf(file, "%lf %lf %lf", &x2, &y2, &z2);
    fscanf(file, "%lf %lf %lf", &x3, &y3, &z3);
    
    fclose(file);

    // Create vectors AB and AC
    M[0][0] = x2 - x1; M[0][1] = x3 - x1; // x components
    M[1][0] = y2 - y1; M[1][1] = y3 - y1; // y components
    M[2][0] = z2 - z1; M[2][1] = z3 - z1; // z components

    // Calculate rank
    int r = rank(M, 3, 2);
    
    if (r < 2) {
        printf("The points are collinear.\n");
    } else {
        printf("The points are not collinear.\n");
    }

    // Free memory
    for (int i = 0; i < 3; i++)
        free(M[i]);
    free(M);
    
    return 0;
}

