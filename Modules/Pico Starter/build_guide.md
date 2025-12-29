# Pico Starter Build Guide

## Bill of Materials (BOM)

| Component | Quantity | Purpose | Notes |
| :--- | :---: | :--- | :--- |
| **Raspberry Pi Pico** | 1 | Brains | Standard header installation. |
| **3.5mm Mono Jack** | 3 | Input, Out A, Out B | Thonkiconn / PJ-301M. |
| **Potentiometer** | 1 | Probability | B100K 9mm Vertical (Linear). |
| **Tactile Button** | 1 | Manual Trigger | 6x6mm standard. |
| **Resistor 100kΩ** | 1 | Input Protection | |
| **Resistor 1kΩ** | 2 | Output Protection | |
| **Diode 1N5817** | 1 | Input Voltage Clamp | Schottky (BAT43/85 also fine). |
| **Electrolytic Cap 10uF** | 1 | Power Rail Filter | |
| **Ceramic Cap 100nF** | 1 | Decoupling | |
| **10-pin Power Header** | 1 | Power Input | Standard IDC. |
| **Schottky Diode** | 1 | Reverse Polarity Protection | 1N5817 on power input (optional but recommended). |

## Schematic / Wiring Logic

Since this is a "Starter" project, we can wire this point-to-point on a small perfboard or even use a breakout board.

### Power
*   **Euro Power +12V** -> (Optional Diode) -> **Pico VSYS Pin** (Pin 39).
    *   *Note: Using VSYS allows the Pico to manage the regulation to 3.3V.*
*   **Euro Power GND** -> **Pico GND** (Pin 38 or any GND).

### Input (Protected)
*   **Jack Tip** -> **100k Resistor** -> **Pico GP15**.
*   **Pico GP15** -> **Diode (Cathode/Line)** -> **3.3V (Pico Pin 36)**.
*   **Pico GP15** -> **Diode (Anode)** -> **GND**.
    *   *Wait, simple clamp:* Connect Diode Anode to GP15, Cathode to 3.3V. This clamps positive spikes. The 100k limits current enough that internal Pico diodes can handle minor negative spikes, but a second diode (Anode to GND, Cathode to GP15) protects against negative voltage fully. **Bumblebee Simple Standard**: Just the 100k and Diode to 3.3V is usually sufficient for learning.
    *   *Revised Simple Protection*: **Jack Tip** -> **100k Resistor** -> **Pico GP15**. **Pico GP15** -> **Diode Anode**, **Diode Cathode** -> **3.3V**.

### Controls
*   **Knob (Probability)**:
    *   Pin 1: **GND**
    *   Pin 2 (Wiper): **Pico GP26 (ADC0)**
    *   Pin 3: **3.3V (Pico Pin 36)**
*   **Button (Manual Trig)**:
    *   Pin 1: **Pico GP14**
    *   Pin 2: **3.3V**
    *   *Note: Code will enable internal Pull-Down.*

### Outputs
*   **Pico GP0** -> **1k Resistor** -> **Jack Tip A** (Out A).
*   **Pico GP1** -> **1k Resistor** -> **Jack Tip B** (Out B).
*   **Jack Sleeves**: All connected to **GND**.

## Step-by-Step

1.  **Prepare the Pico**: Solder male headers facing **DOWN**.
2.  **Panel Components**: Mount Jacks, Pot (Probability), and Button to your faceplate (or cardboard prototype!).
3.  **Power**: Wire the Euro header to the Pico (12V to VSYS, GND to GND). **DOUBLE CHECK POLARITY**.
4.  **Grounds**: Connect all Jack Sleeves, Pot Pin 1, and Power GND together.
5.  **Signal Wiring**:
    *   Wire the Input Protection circuit (Jack -> Resistor -> Pin + Diode).
    *   Wire the Output Resistors (Pin -> Resistor -> Jack).
    *   Wire the Pot and Button.
6.  **Check**: Multimeter beep test for shorts between 12V/GND and 3.3V/GND.

## Testing
1.  Connect to Power Supply (No USB).
2.  Measure 5V and 3.3V pins on the Pico to ensure onboard regulators are working.
3.  Connect USB to Computer.
4.  Flash `main.py`.
5.  Press the button. You should see LEDs on the Pico (if enabled) or measure voltage at the outputs stepping between 0V and 3.3V.
