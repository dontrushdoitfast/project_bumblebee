/*
 *  Arduino Bernoulli Gate
 *  Project Bumblebee
 *  
 *  Hardware:
 *  - D2: Trig In (Interrupt)
 *  - D3: Manual Button (Active Low, Pullup)
 *  - D4: Out A
 *  - D5: Out B
 *  - A0: Probability Pot
 */

// --- CONFIG ---
const int PIN_TRIG_IN = 2;
const int PIN_BTN = 3;
const int PIN_OUT_A = 4;
const int PIN_OUT_B = 5;
const int PIN_PROB = A0;

const int TRIG_LENGTH_MS = 10;

// --- STATE ---
volatile bool trigger_flag = false;
unsigned long last_trig_time = 0;
bool output_active = false;

void setup() {
  pinMode(PIN_OUT_A, OUTPUT);
  pinMode(PIN_OUT_B, OUTPUT);
  
  // Button with Internal Pullup (Ground to trigger)
  pinMode(PIN_BTN, INPUT_PULLUP);
  
  // Interrupt for Clock Input
  // RISING edge detection
  attachInterrupt(digitalPinToInterrupt(PIN_TRIG_IN), onClockISR, RISING);
  
  // Random Seed from floating analog pin
  randomSeed(analogRead(A5));
}

void loop() {
  // Check Trigger Sources
  bool manual_trig = (digitalRead(PIN_BTN) == LOW);
  
  // Check Manual Debounce/State (Simplified)
  static bool last_btn = HIGH;
  if (manual_trig && last_btn == HIGH) {
    trigger_flag = true; // Set flag manually
    delay(5); // Crudest debounce
  }
  last_btn = manual_trig ? LOW : HIGH;
  
  // --- CORE LOGIC ---
  if (trigger_flag) {
    trigger_flag = false; // Reset flag
    processBernoulli();
  }
}

// Interrupt Service Routine
void onClockISR() {
  trigger_flag = true;
}

void processBernoulli() {
  // 1. Read Probability (0-1023)
  int prob = analogRead(PIN_PROB); // 0 = All B, 1023 = All A
  
  // 2. Roll Dice (0-1023)
  long roll = random(0, 1024);
  
  // 3. Decide Output
  int target_pin = -1;
  
  if (roll < prob) {
    target_pin = PIN_OUT_A;
  } else {
    target_pin = PIN_OUT_B;
  }
  
  // 4. Fire Pulse
  digitalWrite(target_pin, HIGH);
  delay(TRIG_LENGTH_MS); // Blocking delay is fine for simple logic
  digitalWrite(target_pin, LOW);
}
