#include <stdio.h>

int main() {
    FILE *file = fopen("points.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Given points and the calculation for k
    int k = -2;  // The value we computed
    
    // Points
    fprintf(file, "Point A: (%d, -10, 3)\n", k);
    fprintf(file, "Point B: (1, -1, 3)\n");
    fprintf(file, "Point C: (3, 5, 3)\n");
    
    // Close the file
    fclose(file);
    
    printf("Points written to points.txt\n");
    
    return 0;
}

