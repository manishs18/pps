/*
"Task 1: Reverse Debugging with GDB
Objective: Practice reverse debugging in GDB.
Steps:
Write C++ code that iterates and modifies an array.
Compile with -g, run in GDB.
Use record, reverse-step, reverse-continue.


*/

#include <stdio.h>

int multiply(int x, int y){
    return x*y;
}


int main(){
    int a = 6, b = 5;
    int result = multiply(a,b);
    printf("x= %d\n", result);
    return 0;
}