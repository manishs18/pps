/*
"What happens when the recurse() function is called in the main() function, 
and why does it result in a segmentation fault?"
*/


#include <stdio.h>

void recurse() {
    recurse();   // Infinite recursion
}

int main() {
    recurse();   // Stack overflow leads to seg fault
    return 0;
}