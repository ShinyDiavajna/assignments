#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

void point_gen(FILE *fptr, double **A, double **B, int no_rows, int no_cols, int num_points) {
    for (int i = 0; i < num_points; i++) {
        double t = (double)i / (num_points - 1);
        double **output = Matadd(A, Matscale(Matsub(B, A, no_rows, no_cols), no_rows, no_cols, t), no_rows, no_cols);
        fprintf(fptr, "%lf,%lf\n", output[0][0], output[1][0]);
        freeMat(output, no_rows);
    }
}

void equi_triangle_gen(double median, FILE *fptr) {
    double side = (2 * median) / sqrt(3);
    double xA = 0, yA = 2*median/3;
    double xB = -side / 2, yB = (-sqrt(3) / 6) * side;
    double xC = side / 2, yC = (-sqrt(3) / 6) * side;

    int m = 2, n = 1;

    double **A = createMat(m, n);
    double **B = createMat(m, n);
    double **C = createMat(m, n);

    A[0][0] = xA;  A[1][0] = yA;
    B[0][0] = xB;  B[1][0] = yB;
    C[0][0] = xC;  C[1][0] = yC;

    point_gen(fptr, A, B, m, n, 20);
    point_gen(fptr, B, C, m, n, 20);
    point_gen(fptr, C, A, m, n, 20);

    freeMat(A, m);
    freeMat(B, m);
    freeMat(C, m);
}

void circle_point_gen(FILE *fptr, double radius, double *center, int num_points) {
    double **output;
    for (int i = 0; i < num_points; i++) {
        double angle = (2 * M_PI * i) / num_points;
        output = createMat(2, 1);
        output[0][0] = center[0] + radius * cos(angle);
        output[1][0] = center[1] + radius * sin(angle);
        fprintf(fptr, "%lf,%lf\n", output[0][0], output[1][0]);
        freeMat(output, 2);
    }
}

int main() {
    double a = 1.0; //for graphing
    double median = 3*a;
    double radius = 2*a; 
    double center[2] = {0.0, 0.0};

    FILE *fptr = fopen("points.dat", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    equi_triangle_gen(median, fptr);
    circle_point_gen(fptr, radius, center, 100);

    fclose(fptr);
    return 0;
}
