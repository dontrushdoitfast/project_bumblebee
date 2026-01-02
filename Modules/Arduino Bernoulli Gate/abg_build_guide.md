# Arduino Bernoulli Gate Build Guide

## Bill of Materials
*   **Microcontroller**: **1x** Arduino Nano (or Uno/Pro Mini). **(Plus 2x 15-pin Female Headers for socketing)**.
    *   *Clone Note*: Ensure it uses the CH340 driver if applicable.
*   **Jacks**: **3x** 3.5mm Mono (Panel Mount).
*   **Potentiometer**: **1x** B10k or B100k Linear (16mm Panel Mount).
*   **Button**: **1x** Tactile Switch (Panel Mount preferred, or PCB mounted behind panel).
*   **Wiring**: Ribbon cable or stranded wire to connect Panel components to Logic Board.
*   **Resistors**:
    *   **1x** 100k (Input Protection).
    *   **2x** 1k (Output Output Protection).
*   **Power**:
    *   **1x** 10-pin Male Power Header.
    *   **1x** L7805 CV (5V Regulator) + 10uF Cap. *(Optional: Can use Arduino Onboard VIN for 12V, but L7805 is safer/cooler).*

### Construction Note: Split Board
This module works best as two parts:
1.  **Panel**: Holds Jacks, Pot, and Button.
2.  **Logic Board**: Holds Arduino, Resistors, Power Regulator.
*Connect them with flying wires.*

## Wiring Diagram

### 1. Power (The Safer Way)
Do not trust the Clone Arduino's onboard regulator with 12V for long periods.
*   **Euro +12V** -> **L7805 In**.
*   **L7805 Out (5V)** -> **Arduino 5V Pin**.
*   **Euro GND** -> **Arduino GND**.
*   *Add 10uF Capacitor between +12V and GND.*

### 2. Input (Interrupt)
We use **Pin 2** (Interrupt 0) for the Trigger Input.
```
  [Jack Tip] ──► [100k Resistor] ──┬──► [Arduino D2]
                                   │
                                 [Diode] (Optional Clamping to 5V)
```
*Note: The Arduino's internal diodes + 100k resistor are usually sufficient for standard Eurorack signals.*

### 3. Outputs
Direct drive from digital pins.
*   **Arduino D4** ──► [1k Resistor] ──► [Jack Tip A]
*   **Arduino D5** ──► [1k Resistor] ──► [Jack Tip B]

### 4. Controls
*   **Potentiometer**:
    *   Pin 1: GND
    *   Pin 2: **Arduino A0**
    *   Pin 3: 5V
*   **Button** (Manual Trig):
    *   Pin 1: **Arduino D3**
    *   Pin 2: GND
    *   *Note: Use INPUT_PULLUP in code. Logic is Inverted (LOW = Pressed).*

## Code Upload
1.  Install Arduino IDE.
2.  Select Board: "Arduino Nano".
3.  Processor: "ATmega328P (Old Bootloader)" is common for clones.
4.  Upload the `abg_firmware.ino`.
