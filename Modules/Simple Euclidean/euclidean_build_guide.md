# Simple Euclidean Build Guide

## Bill of Materials (BOM)
*Identical to the Bernoulli Gate Build.*

| Component | Quantity | Purpose | Notes |
| :--- | :---: | :--- | :--- |
| **Raspberry Pi Pico** | 1 | Brains | Standard header installation. **Use 2x 20-pin Female Headers**. |
| **3.5mm Mono Jack** | 3 | Input, Out A, Out B | Thonkiconn / PJ-301M. |
| **Potentiometer** | 1 | Density | B100K 9mm Vertical (Linear). |
| **Tactile Button** | 1 | Reset / Tap | 6x6mm standard. |
| **Resistor 100kΩ** | 1 | Input Protection | |
| **Resistor 1kΩ** | 2 | Output Protection | |
| **Diode 1N5817** | 1 | Input Voltage Clamp | Schottky. |
| **10-pin Power Header** | 1 | Power Input | Standard IDC. |
| **10uF Capacitor** | 1 | Power Filtering | |

## Wiring Logic

### Power
*   **Euro Power +12V** -> **Pico VSYS** (Pin 39).
*   **Euro Power GND** -> **Pico GND** (Pin 38).

### Input (Protected)
*   **Jack Tip** -> **100k Resistor** -> **Pico GP15**.
*   **Pico GP15** -> **Diode Anode**. **Diode Cathode** -> **3.3V**.

### Controls
*   **Knob (Density)**:
    *   Pin 1: GND
    *   Pin 2 (Wiper): **Pico GP26 (ADC0)**
    *   Pin 3: 3.3V
*   **Button (Reset)**:
    *   Pin 1: **Pico GP14**
    *   Pin 2: 3.3V (Active High, will use Pull-Down)

### Outputs
*   **Pico GP0** -> **1k Resistor** -> **Jack Tip A** (Pattern).
*   **Pico GP1** -> **1k Resistor** -> **Jack Tip B** (Inverse).

## Code Logic
*   **Steps**: Fixed at 16.
*   **Input**: Advances current `step` index (0-15).
*   **Knob**: Maps 0V-3.3V to `hits` (0 to 16).
*   **Algorithm**: Bjorklund / Bresenham algorithm logic.
