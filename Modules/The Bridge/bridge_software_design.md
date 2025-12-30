# The Bridge Software Design

## Overview
This module acts as a **USB MIDI Device**. It receives MIDI packets from the Host (DAW) and updates the DAC/GPIOs immediately.
It does **NOT** use the standard MicroPython `usb_midi` library (which can be tricky on Pico W). We will use `tinyusb` or the built-in MIDI support if available, or simpler: classic UART MIDI if we used a DIN jack. But for USB, we rely on the **Adafruit CircuitPython** or **C++** stack usually.
*DECISION*: To stick with **MicroPython**, we might need a custom build or extensive library support.
*SIMPLER ALTERNATIVE*: We code this one in **CircuitPython**. CircuitPython has native, perfect USB MIDI support out of the box.

**Strategy**: Use **CircuitPython** for this module. It is Python, but with better USB libraries.

## Logic Flow
1.  **Boot**: Initialize USB MIDI Class. Setup SPI for MCP4822.
2.  **Loop**:
    *   Check `midi.receive()`.
    *   If **Note On (Ch 1)**:
        *   Map Midi Note (0-127) to Voltage (0-10V).
        *   Value = (Note - Offset) * ScaleFactor.
        *   Send to CV A (DAC A).
        *   Set Gate 1 HIGH.
    *   If **Note Off (Ch 1)**:
        *   Set Gate 1 LOW.
    *   If **CC (Mod Wheel)**:
        *   Map 0-127 to 0-10V.
        *   Send to CV B (DAC B).

## Calibration (Software)
Hardware resistors vary. We need a software correction.
*   `GAIN_A = 1.02`
*   `OFFSET_A = -0.01`
*   The code should apply these before sending to the DAC.

## DAC Driver (MCP4822)
*   **Protocol**: SPI.
*   **Command**: 16-bit word.
    *   Bit 15: A/B Select.
    *   Bit 14: Buffered? (Yes).
    *   Bit 13: Gain? (1x).
    *   Bit 12: Shutdown? (Active).
    *   Bits 11-0: Data (0-4095).
