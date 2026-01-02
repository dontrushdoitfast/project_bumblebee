# The Bridge (USB MIDI to CV) Description

**Difficulty: ⭐⭐⭐ Moderate** — *Involves Digital (Pico), DACs, and precise calibration.*

### Description
**The Bridge** is the link between your computer (Logic Pro) and your Eurorack system (2600/Proton).
Instead of relying on the Behringer's internal mono/duo logic, this module provides discrete, dedicated channels for **Pitch** and **Modulation** that you can automate precisely from your DAW.

### Requirements
1.  **USB MIDI**: Connects as a Class Compliant MIDI Device via the Pico's USB port.
2.  **Outputs**:
    *   **CV A (Pitch/Mod)**: 0-10V Precision Analog (12-bit).
    *   **CV B (Pitch/Mod)**: 0-10V Precision Analog (12-bit).
    *   **Gates 1-4**: 5V Digital Triggers/Gates.
3.  **Configurability**: Default mapping (Channel 1 Note -> CV A/Gate 1) should be sensible, but code can be tweaked.

### Panel Layout
*   **Width**: 6HP
*   **Top**: USB C Port (Panel mount extension).
*   **Jacks**:
    *   CV A | CV B
    *   Gate 1 | Gate 2
    *   Gate 3 | Gate 4

### Technical Specifications
*   **Core**: Raspberry Pi Pico (RP2040).
*   **DAC**: MCP4822 (Dual channel, 12-bit, SPI).
    *   *Note*: The MCP4822 has an internal reference (2.048V). We use an Op-Amp with gain (x2 approx) to boost this to 0-5V standard.
*   **Power**: Standard +/-12V via **10-pin Header**. (5V/3.3V generated onboard).
*   **Gate Outputs**: Direct GPIO via 1k protection resistors.
