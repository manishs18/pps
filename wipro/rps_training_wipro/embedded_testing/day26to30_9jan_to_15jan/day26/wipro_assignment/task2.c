/*

Task 1: Logical Error Resolution
Objective: Find and fix a logical error using GDB.
Steps: 
Use C code with a know bug.
Compile, start GDB, set breakpoint.
Identify error, edit code, recompile, confirm fix.

*/

#include <stdio.h>

int multiply(int a, int b){
    return a+b;
}

int main(){
    int x = 3, y = 4;
    int result = multiply(x,y);
    printf("Product: %d\n", result);
    return 0;
}