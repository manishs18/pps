void setup() {
  Serial.begin(9600);  // Start serial communication
 
  // Configure GPIO pins
  pinMode(2, OUTPUT);  // LED1
  pinMode(3, OUTPUT);  // LED2
  pinMode(4, INPUT_PULLUP); // Push Button with internal pull-up resistor
  pinMode(5, OUTPUT);  // Loopback Output
  pinMode(6, INPUT);   // Loopback Input


  Serial.println("Boundary Scan Test Starting...");
}


void loop() {
  // Test LED1 (Pin 2)
  digitalWrite(2, HIGH);  // Turn on LED1
  delay(500);
  Serial.println("Test 1: LED1 ON");
  digitalWrite(2, LOW);   // Turn off LED1
  delay(500);


  // Test LED2 (Pin 3)
  digitalWrite(3, HIGH);  // Turn on LED2
  delay(500);
  Serial.println("Test 2: LED2 ON");
  digitalWrite(3, LOW);   // Turn off LED2
  delay(500);


  // Test Push Button (Pin 4)
  int buttonState = digitalRead(4);  // Read the button state
  if (buttonState == LOW) {  // Button pressed
    Serial.println("Test 3: Push Button PRESSED");
  } else {  // Button not pressed
    Serial.println("Test 3: Push Button NOT PRESSED");
  }
  delay(500);


  // Test Loopback (Pin 5 to Pin 6)
  digitalWrite(5, HIGH);  // Send HIGH signal from Pin 5
  delay(100);
  int loopbackState = digitalRead(6);  // Read signal on Pin 6
  if (loopbackState == HIGH) {
    Serial.println("Test 4: Loopback Test PASSED (HIGH detected)");
  } else {
    Serial.println("Test 4: Loopback Test FAILED (HIGH not detected)");
  }


  digitalWrite(5, LOW);  // Send LOW signal from Pin 5
  delay(100);
  loopbackState = digitalRead(6);  // Read signal on Pin 6 again
  if (loopbackState == LOW) {
    Serial.println("Test 5: Loopback Test PASSED (LOW detected)");
  } else {
    Serial.println("Test 5: Loopback Test FAILED (LOW not detected)");
  }


  delay(1000);  // Wait before restarting the tests
}
