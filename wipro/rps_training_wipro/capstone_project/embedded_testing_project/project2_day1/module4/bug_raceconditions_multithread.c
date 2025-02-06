#include <stdio.h>
#include <pthread.h>

int shared_counter = 0;  // Shared variable
void *increment(void *arg) {
    for (int i = 0; i < 10; i++) {
        shared_counter++;  // Increment the shared variable
        printf("Incrementing: Counter = %d\n", shared_counter);
    }
    return NULL;
}
void *decrement(void *arg) {
    for (int i = 0; i < 10; i++) {
        shared_counter--;  // Decrement the shared variable
        printf("Decrementing: Counter = %d\n", shared_counter);
    }
    return NULL;
}
int main() {
    pthread_t thread1, thread2;
    // Create two threads: one for incrementing and one for decrementing
    pthread_create(&thread1, NULL, increment, NULL);
    pthread_create(&thread2, NULL, decrement, NULL);
    // Wait for both threads to finish
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    printf("Final Counter Value: %d\n", shared_counter);
    return 0;
}
