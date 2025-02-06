#include <stdio.h>
#include <string.h>

void vulnerableFunction(char *str) {
    char buffer[10];
    // The following line introduces a buffer overflow vulnerability.
    strcpy(buffer, str);
}
int main() {
    // Input string larger than the allocated buffer size.
    char largeInput[] = "TooLongInputDataExceedingBuffer";
    vulnerableFunction(largeInput);
    return 0;
}