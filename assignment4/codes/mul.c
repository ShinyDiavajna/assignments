#include <stdio.h>
#include <stdbool.h>
#include<stdlib.h>

#define ROWS 2
#define COLS 3

// Function to perform Gaussian Elimination and find the rank of the matrix
int findRank(int matrix[ROWS][COLS]) {
    int rank = COLS; // Initialize rank as the number of columns
    int row, col, i, j;

    // Perform Gaussian Elimination
    for (row = 0; row < rank; ++row) {
        // Search for maximum element in the current column
        int maxRow = row;
        for (i = row + 1; i < ROWS; ++i) {
            if (abs(matrix[i][row]) > abs(matrix[maxRow][row])) {
                maxRow = i;
            }
        }

        // Swap maximum row with the current row
        if (matrix[maxRow][row] != 0) {
            if (maxRow != row) {
                for (j = 0; j < rank; ++j) {
                    int temp = matrix[row][j];
                    matrix[row][j] = matrix[maxRow][j];
                    matrix[maxRow][j] = temp;
                }
            }

            // Eliminate column entries below the pivot
            for (i = row + 1; i < ROWS; ++i) {
                if (matrix[i][row] != 0) {
                    double ratio = (double)matrix[i][row] / matrix[row][row];
                    for (j = row; j < rank; ++j) {
                        matrix[i][j] -= ratio * matrix[row][j];
                    }
                }
            }
        } else {
            // If the pivot element is zero, reduce the rank
            --rank;
            for (i = 0; i < ROWS; ++i) {
                matrix[i][row] = matrix[i][rank];
            }
            --row;
        }
    }

    // Count non-zero rows
    int rankCount = 0;
    for (i = 0; i < ROWS; ++i) {
        bool nonZero = false;
        for (j = 0; j < COLS; ++j) {
            if (matrix[i][j] != 0) {
                nonZero = true;
                break;
            }
        }
        if (nonZero) {
            ++rankCount;
        }
    }

    return rankCount;
}


