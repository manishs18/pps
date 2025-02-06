#include <stdio.h>
#include <pthread.h>

int shared_counter = 0;  // Shared variable
pthread_mutex_t lock;    // Mutex lock
void *increment(void *arg) {
    for (int i = 0; i < 10; i++) {
        pthread_mutex_lock(&lock);
        shared_counter++;  // Safely increment
        printf("Incrementing: Counter = %d\n", shared_counter);
        pthread_mutex_unlock(&lock);
    }
    return NULL;
}
void *decrement(void *arg) {
    for (int i = 0; i < 10; i++) {
        pthread_mutex_lock(&lock);
        shared_counter--;  // Safely decrement
        printf("Decrementing: Counter = %d\n", shared_counter);
        pthread_mutex_unlock(&lock);
    }
    return NULL;
}
int main() {
    pthread_t thread1, thread2;
    pthread_mutex_init(&lock, NULL);  // Initialize the mutex
    // Create threads
    pthread_create(&thread1, NULL, increment, NULL);
    pthread_create(&thread2, NULL, decrement, NULL);
    // Wait for threads to finish
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    pthread_mutex_destroy(&lock);  // Destroy the mutex
    printf("Final Counter Value: %d\n", shared_counter);
    return 0;
}
