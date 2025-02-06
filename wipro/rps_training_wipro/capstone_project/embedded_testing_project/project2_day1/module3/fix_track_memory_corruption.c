#include <stdio.h>
#include <string.h>

void safeFunction(char *str) {
    char buffer[10];
    // Use strncpy to prevent buffer overflow.
    strncpy(buffer, str, sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = '\0'; // Ensure null termination.
    printf("Buffer content: %s\n", buffer);
}
int main() {
    // Input string larger than the allocated buffer size.
    char largeInput[] = "TooLongInputDataExceedingBuffer";
    safeFunction(largeInput);
    return 0;
}
