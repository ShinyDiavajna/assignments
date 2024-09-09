#include <stdio.h>

int main() {
    // Define the filename
    const char *filename = "plot1.txt";

    // Open the file for writing (create it if it doesn't exist)
    FILE *file = fopen(filename, "w");

    // Check if the file was created/opened successfully
    if (file == NULL) {
        perror("Error opening file");
        return 1; // Return a non-zero value to indicate failure
    }

    // Write the coordinates to the file
    fprintf(file, "Points for plotting:\n");
    fprintf(file, "Point P: (2, 1)\n");
    fprintf(file, "Point A: (4, 2)\n");
    fprintf(file, "Point B: (8, 4)\n");

    // Optional: Write points in a format that might be useful for some plotting libraries
    fprintf(file, "\nX,Y\n");
    fprintf(file, "2,1\n");
    fprintf(file, "4,2\n");
    fprintf(file, "8,4\n");

    // Close the file
    fclose(file);

    printf("File '%s' has been created and data has been written.\n", filename);

    return 0; // Return 0 to indicate success
}

