#define RCC_AHB1ENR    *((volatile unsigned int*)0x40023830)  // RCC AHB1 peripheral clock enable register
#define GPIOA_MODER    *((volatile unsigned int*)0x40020000)  // GPIOA mode register
#define GPIOA_ODR      *((volatile unsigned int*)0x40020014)  // GPIOA output data register

#define RCC_AHB1ENR_GPIOAEN (1 << 0)  // GPIOA clock enable bit
#define GPIO_MODER_MODER5_0 (1 << 10) // PA5 mode (output)

void delay(volatile unsigned int count) {
    while (count--) {
        // Empty loop to create delay
    }
}

extern "C" void _exit(int status) {
    while (1) {
        // Do nothing, just loop forever
    }
}

int main() {
    // Enable GPIOA clock
    RCC_AHB1ENR |= RCC_AHB1ENR_GPIOAEN;

    // Set PA5 as output
    GPIOA_MODER |= GPIO_MODER_MODER5_0;  // PA5 output mode

    while (1) {
        GPIOA_ODR |= (1 << 5);   // Turn on LED (PA5 high)
        delay(1000000);          // Delay
        GPIOA_ODR &= ~(1 << 5);  // Turn off LED (PA5 low)
        delay(1000000);          // Delay
    }
}
