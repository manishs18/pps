int input_pin = 2;
volatile int valume = 0;

void setupTimer1() {
  noInterrupts();
  TCCR1A = 0;
  TCCR1B = 0;
  TCNT1 = 0;

  OCR1A = 31249; // ค่าที่ถูกต้องสำหรับ 0.5 Hz
  TCCR1B |= (1 << WGM12);   // CTC mode
  TCCR1B |= (1 << CS12) | (1 << CS10); // Prescaler 1024
  TIMSK1 |= (1 << OCIE1A);  // เปิดใช้งาน Interrupt
  interrupts();
}

void setupTimer3() {
  noInterrupts();
  TCCR3A = 0;
  TCCR3B = 0;
  TCNT3 = 0;

  OCR3A = 15624; // ค่าที่ถูกต้องสำหรับ 1 Hz
  TCCR3B |= (1 << WGM32);
  TCCR3B |= (1 << CS32) | (1 << CS30);
  TIMSK3 |= (1 << OCIE3A);
  interrupts();
}

void setup() {
  pinMode(input_pin, INPUT);
  attachInterrupt(digitalPinToInterrupt(input_pin), state, FALLING);
  DDRC = 0xFF;
  setupTimer1();
  setupTimer3();
  Serial.begin(9600);
}

void loop() {
  PORTC = (1 << PC7);
  delay(1000);
  PORTC = (0 << PC7);
  delay(1000);
}

void state() {
  static unsigned long lastInterruptTime = 0;
  unsigned long interruptTime = millis();

  if (interruptTime - lastInterruptTime > 500) { // Debounce
    valume++;
    if (valume > 3) valume = 1; // รีเซ็ต state
    Serial.print("State: ");
    Serial.println(valume);
  }

  lastInterruptTime = interruptTime;
}

ISR(TIMER1_COMPA_vect) {
  if (valume == 1) {
    PORTC ^= (1 << PC6) | (1 << PC5) | (1 << PC4);
  }
}

ISR(TIMER3_COMPA_vect) {
  if (valume == 2) {
    PORTC ^= (1 << PC3) | (1 << PC2) | (1 << PC1) | (1 << PC0);
  }
}
