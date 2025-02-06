/*
"What happens when accessing an out-of-bounds array element like arr[10], 
and why is it problematic?"

*/

#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    printf("%d\n", arr[10]);    //Accessing out-of-bounds memory
    return 0;
}
