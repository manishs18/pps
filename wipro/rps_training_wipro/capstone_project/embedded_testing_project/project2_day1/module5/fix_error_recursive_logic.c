#include <stdio.h>

void fixedRecursion(int n) {
    if (n > 10) return;  // Base case to stop recursion
    printf("Recursion level: %d\n", n);
    fixedRecursion(n + 1);  // Recursive call with proper base case
}

int main() {
    fixedRecursion(1);  // Start recursion
    return 0;
}