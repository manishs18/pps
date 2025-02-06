#include <Arduino.h>

TaskHandle_t Task1Handle = NULL;

void setup() {
    Serial.begin(115200);
    delay(1000);
    Serial.println("ESP32 Setup Complete");

    // Create a FreeRTOS task with a different name
    xTaskCreate(myLoopTask, "Loop Task", 10000, NULL, 1, &Task1Handle);
}

void loop() {
    // Empty loop as FreeRTOS tasks are running in the background
}

void myLoopTask(void *pvParameters) {
    while (1) {
        // Task logic
        Serial.println("Loop Task is running...");
        vTaskDelay(1000 / portTICK_PERIOD_MS);  // Delay for 1 second
    }
}
