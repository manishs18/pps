/*

Task 1: Basic Debugging with GDB
Objective: Use GDB to step through a simple program.
Steps: 
Write a basic C sum function.
Compile with -g, start GDB.
Set breakpooint, run, step, print variables.

*/

#include <stdio.h>


int sum(int a, int b){
    return a+b;
}

int main() {
    int x = 42, y=4;
    int result = sum(x,y);
    printf("x = %d\n", result);
    return 0;
    
}