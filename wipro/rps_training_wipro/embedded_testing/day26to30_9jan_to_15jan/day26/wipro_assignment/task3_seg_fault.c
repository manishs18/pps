/*

Task 3: Segmentation Fault Analysis
Objective: Identify cause of a segmentation fault.
Steps:
Start with crash-prone C code.
Run in GDB, trigger crash.
Backtrace, inspect variables at fault."

*/
#include <stdio.h>


int main(){
    int *ptr = NULL; // Pointer initialized to NULL
    *ptr = 42;    //Attempt to dereference NULL pointer
    printf("Value at ptr: %d\n", *ptr);
}