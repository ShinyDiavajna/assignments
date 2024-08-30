#include<stdio.h>

int main() {
	int ROWS = 2;
	int COLS = 3;
	int matrix[ROWS][COLS] = {
	  {1,-4,-2},
	  {-3,12,6}

	};

	printf("Rank of the matrix is : %d\n",findRank(matrix));

	return 0;
}
