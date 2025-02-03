#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


typedef struct Node {
    void (*handler)(const char*); 
    struct Node* next;            
} Node;

typedef struct {
    Node* head;  
} Event;
void event_initialize(Event* event) {
    event->head = NULL;
}
bool event_subscribe(Event* event, void (*handler)(const char*)) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    if (!new_node) return false;

    new_node->handler = handler;
    new_node->next = event->head;
    event->head = new_node;
    return true;
}
void event_notify(Event* event, const char* message) {
    Node* current = event->head;
    while (current) {
        current->handler(message);  
        current = current->next;
    }
}
void event_deinitialize(Event* event) {
    Node* current = event->head;
    while (current) {
        Node* temp = current;
        current = current->next;
        free(temp);
    }
    event->head = NULL;
}
void handler1(const char* message) {
    printf("Handler 1 received: %s\n", message);
}
void handler2(const char* message) {
    printf("Handler 2 received: %s\n", message);
}
int main() {
    Event event;
    event_initialize(&event);
    event_subscribe(&event, handler1);
    event_subscribe(&event, handler2);
    printf("Notifying handlers...\n");
    event_notify(&event, "Hello, Handlers!");
    event_deinitialize(&event);
    return 0;
}
