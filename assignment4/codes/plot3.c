#include <stdio.h>

int main() {
    // Define the coordinates of the points
    int points[3][3] = {
        {2, -1, 3},   // Point 1
        {3, -5, 1},   // Point 2
        {-1, 11, 9}    // Point 3
    };

    // Open a file in write mode
    FILE *file = fopen("plot3.txt", "w");
    if (file == NULL) {
        // Error handling in case the file cannot be opened
        printf("Error opening file!\n");
        return 1;
    }

    // Write the points to the file
    for (int i = 0; i < 3; i++) {
        fprintf(file, "Point %d: (%d, %d, %d)\n", i + 1, points[i][0], points[i][1], points[i][2]);
    }

    // Close the file
    fclose(file);


    return 0;
}

