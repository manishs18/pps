/* ESP32 WiFi Scanning example */

#include "WiFi.h"

void setup() {
  Serial.begin(115200);
  Serial.println("Initializing WiFi...");
  WiFi.mode(WIFI_STA);
  Serial.println("Setup done!");
}

void loop() {
  Serial.println("Scanning...");

  // WiFi.scanNetworks will return the number of networks found
  int n = WiFi.scanNetworks();
  Serial.println("Scan done!");
  if (n == 0) {
    Serial.println("No networks found.");
  } else {
    Serial.println();
    Serial.print(n);
    Serial.println(" networks found");
    for (int i = 0; i < n; ++i) {
      // Print SSID and RSSI for each network found
      Serial.print(i + 1);
      Serial.print(": ");
      Serial.print(WiFi.SSID(i));
      Serial.print(" (");
      Serial.print(WiFi.RSSI(i));
      Serial.print(")");
      Serial.println((WiFi.encryptionType(i) == WIFI_AUTH_OPEN) ? " " : "*");
      delay(10);
    }
  }
  Serial.println("");

  // Wait a bit before scanning again
  delay(5000);
}



/*
 This gbd commands are used to debug the code for ESP32 using OpenOCD and GDB.

(gdb) target remote localhost:3333           # Connect to ESP32 target via OpenOCD
(gdb) monitor reset halt                     # Reset the ESP32 and halt it
(gdb) load                                     # Load the program onto the ESP32
(gdb) break main                               # Set breakpoint at main()
(gdb) run                                      # Run the program
(gdb) info breakpoints                        # List breakpoints
(gdb) watch DWT_CYCCNT                        # Set a watchpoint on the cycle counter
(gdb) continue                                # Let the program run
(gdb) info watchpoints                        # Inspect triggered watchpoints
(gdb) step                                    # Step through the program
(gdb) info registers                          # Inspect CPU registers
(gdb) x/10x $sp                               # Examine stack pointer memory


*/