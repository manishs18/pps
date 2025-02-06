#include <stdio.h>
#include <stdlib.h>

int main() {
    int *array = NULL;
    int n = 5;

    // Logical error: Conditional  that skips memory allocation
    if(n < 0){
        array = malloc(n * sizeof(int));
    }
    // Attempting to dereference a NULL pointer
    array[0] = 10; // Causes segmentation fault
    printf("Value at index 0: %d\n", array[0]);
    free(array); //Free allocated memory
    return 0;
}