#include <stdio.h>

int main() {
    int value = 42;
    int *ptr = &value;   //initialize ppinter to a point
    *ptr = 42;            //Attempt to dereference NULL pointer
    printf("Value at ptr: %d\n", *ptr);
    return 0;
}