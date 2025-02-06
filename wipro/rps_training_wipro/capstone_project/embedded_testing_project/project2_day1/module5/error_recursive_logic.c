#include <stdio.h>

void faultyRecursion(int n) {
    printf("Recursion level: %d\n", n);
    faultyRecursion(n + 1);  // Incorrect base case, no termination condition
}

int main() {
    faultyRecursion(1);  // Start recursion
    return 0;
}
