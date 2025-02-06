#include <stdio.h>

int main(){
    int n = 5;  //calculate factorial of 5
    int factorial = 1;

    //logical error: Incorrect initialization of the loop variable
    for(int i = 0; i <= n; i++){
        factorial *= i;   //causes multiplication by 0 in the first iteration
    }
    printf("Factorial of %d is %d\n", n, factorial);
    return 0;
}