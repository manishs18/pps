
#define TCK_PIN 2 // Test Clock
#define TMS_PIN 3 // Test Mode Select


// LED Pins for representing states
#define LED_1 8  // TEST_LOGIC_RESET
#define LED_2 9  // RUN_TEST_IDLE
#define LED_3 10 // SELECT_DR_SCAN
#define LED_4 11 // CAPTURE_DR
#define LED_5 12 // UPDATE_IR


enum TAP_State {
  TEST_LOGIC_RESET,
  RUN_TEST_IDLE,
  SELECT_DR_SCAN,
  CAPTURE_DR,
  SHIFT_DR,
  EXIT1_DR,
  PAUSE_DR,
  EXIT2_DR,
  UPDATE_DR,
  SELECT_IR_SCAN,
  CAPTURE_IR,
  SHIFT_IR,
  EXIT1_IR,
  PAUSE_IR,
  EXIT2_IR,
  UPDATE_IR
};


TAP_State currentState = TEST_LOGIC_RESET;
bool lastTckState = LOW; // To track the previous state of TCK


void setup() {
  // Button input pins
  pinMode(TCK_PIN, INPUT);
  pinMode(TMS_PIN, INPUT);


  // LED output pins
  pinMode(LED_1, OUTPUT);
  pinMode(LED_2, OUTPUT);
  pinMode(LED_3, OUTPUT);
  pinMode(LED_4, OUTPUT);
  pinMode(LED_5, OUTPUT);


  // Initialize Serial Monitor
  Serial.begin(9600);
  Serial.println("Starting JTAG TAP Controller Simulation");
  indicateState(currentState); // Indicate the initial state with LEDs
}


void loop() {
  bool tms = digitalRead(TMS_PIN);  // Read TMS state
  bool tck = digitalRead(TCK_PIN);  // Read TCK state


  // Debugging button states
  Serial.print("TMS: ");
  Serial.print(tms);
  Serial.print(" | TCK: ");
  Serial.println(tck);


  // Detect rising edge of TCK
  if (tck == HIGH && lastTckState == LOW) { // Rising edge detected
    Serial.println("Rising edge detected on TCK");


    // Print the current state before transition
    Serial.print("Previous State: ");
    Serial.println(stateToString(currentState));


    // Perform state transition based on TMS input
    switch (currentState) {
      case TEST_LOGIC_RESET:
        currentState = tms ? TEST_LOGIC_RESET : RUN_TEST_IDLE;
        break;
      case RUN_TEST_IDLE:
        currentState = tms ? SELECT_DR_SCAN : RUN_TEST_IDLE;
        break;
      case SELECT_DR_SCAN:
        currentState = tms ? SELECT_IR_SCAN : CAPTURE_DR;
        break;
      case CAPTURE_DR:
        currentState = tms ? EXIT1_DR : SHIFT_DR;
        break;
      case SHIFT_DR:
        currentState = tms ? EXIT1_DR : SHIFT_DR;
        break;
      case EXIT1_DR:
        currentState = tms ? UPDATE_DR : PAUSE_DR;
        break;
      case PAUSE_DR:
        currentState = tms ? EXIT2_DR : PAUSE_DR;
        break;
      case EXIT2_DR:
        currentState = tms ? UPDATE_DR : SHIFT_DR;
        break;
      case UPDATE_DR:
        currentState = tms ? SELECT_DR_SCAN : RUN_TEST_IDLE;
        break;
      case SELECT_IR_SCAN:
        currentState = tms ? TEST_LOGIC_RESET : CAPTURE_IR;
        break;
      case CAPTURE_IR:
        currentState = tms ? EXIT1_IR : SHIFT_IR;
        break;
      case SHIFT_IR:
        currentState = tms ? EXIT1_IR : SHIFT_IR;
        break;
      case EXIT1_IR:
        currentState = tms ? UPDATE_IR : PAUSE_IR;
        break;
      case PAUSE_IR:
        currentState = tms ? EXIT2_IR : PAUSE_IR;
        break;
      case EXIT2_IR:
        currentState = tms ? UPDATE_IR : SHIFT_DR;
        break;
      case UPDATE_IR:
        currentState = tms ? SELECT_DR_SCAN : RUN_TEST_IDLE;
        break;
    }


    // Indicate the new state with LEDs
    indicateState(currentState);


    // Print the new state to Serial Monitor
    Serial.print("New State: ");
    Serial.println(stateToString(currentState));
  }


  // Update last TCK state
  lastTckState = tck;


  delay(50); // Add a small delay to stabilize input readings
}


// Function to control LEDs based on the current state
void indicateState(TAP_State state) {
  // Turn off all LEDs
  digitalWrite(LED_1, LOW);
  digitalWrite(LED_2, LOW);
  digitalWrite(LED_3, LOW);
  digitalWrite(LED_4, LOW);
  digitalWrite(LED_5, LOW);


  // Turn on the LED corresponding to the current state
  switch (state) {
    case TEST_LOGIC_RESET:
      digitalWrite(LED_1, HIGH);
      break;
    case RUN_TEST_IDLE:
      digitalWrite(LED_2, HIGH);
      break;
    case SELECT_DR_SCAN:
      digitalWrite(LED_3, HIGH);
      break;
    case CAPTURE_DR:
      digitalWrite(LED_4, HIGH);
      break;
    case UPDATE_IR:
      digitalWrite(LED_5, HIGH);
      break;
    default:
      break; // Handle additional states as needed
  }
}


// Function to return a string representation of the current state
String stateToString(TAP_State state) {
  switch (state) {
    case TEST_LOGIC_RESET: return "Test-Logic-Reset";
    case RUN_TEST_IDLE: return "Run-Test/Idle";
    case SELECT_DR_SCAN: return "Select-DR-Scan";
    case CAPTURE_DR: return "Capture-DR";
    case SHIFT_DR: return "Shift-DR";
    case EXIT1_DR: return "Exit1-DR";
    case PAUSE_DR: return "Pause-DR";
    case EXIT2_DR: return "Exit2-DR";
    case UPDATE_DR: return "Update-DR";
    case SELECT_IR_SCAN: return "Select-IR-Scan";
    case CAPTURE_IR: return "Capture-IR";
    case SHIFT_IR: return "Shift-IR";
    case EXIT1_IR: return "Exit1-IR";
    case PAUSE_IR: return "Pause-IR";
    case EXIT2_IR: return "Exit2-IR";
    case UPDATE_IR: return "Update-IR";
    default: return "Unknown State";
  }
}
