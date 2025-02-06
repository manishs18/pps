/*
"What does this Arduino code do, and how does it control the LEDs connected to pins 8 and 9?"


*/
void setup() {
  pinMode(8, OUTPUT); // Set pin 8 as output for LED 1
  pinMode(9, OUTPUT); // Set pin 9 as output for LED 2
}

void loop() {
  digitalWrite(8, HIGH); // Turn on LED 1
  digitalWrite(9, LOW);  // Turn off LED 2
  delay(500);            // Wait for 500ms
  
  digitalWrite(8, LOW);  // Turn off LED 1
  digitalWrite(9, HIGH); // Turn on LED 2
  delay(500);            // Wait for 500ms
}


