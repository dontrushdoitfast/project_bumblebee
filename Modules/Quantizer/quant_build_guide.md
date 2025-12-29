# Quantizer Build Guide

### Overview
This build guides you through creating a precision **Quantizer** using the Raspberry Pi Pico and the MCP4725 DAC. It replaces the classic PWM approach with a dedicated I2C DAC for stable pitch generation.

### Tools needed
*   **Soldering Iron**
*   **Computer** (MicroPython)
*   **Wire Strippers**
*   **Multimeter** (Essential for calibration)

### Bill Of Materials
*   **Microcontroller**: **1x** Raspberry Pi Pico.
*   **DACs**: **2x** MCP4725 Breakout Boards (I2C).
    *   *Mod Required*: On the second board, bridge the "A0" pad to change address to `0x61`.
*   **User Input**:
    *   **12x** Tactile Buttons (6x6mm).
    *   **12x** PL9823 (or APA106) 5mm RGB LEDs (Through-hole NeoPixels).
    *   **2x** Rotary Knobs + B100k Linear Pots.
*   **Jacks**: **4x** Thonkiconn PJ-301M-12 (CV In A, CV In B, CV Out A, CV Out B).
*   **Power**:
    *   **1x** L7805 CV (5V Regulator).
    *   **1x** 10uF Electrolytic Capacitor (Power bypass).
    *   **1x** 10-pin Eurorack Power Header.
*   **Protection (Standard Bumblebee Prototcols)**:
    *   **Inputs (x2)**: **100k** Series Resistor + **1N5817** Schottky Diode (Clamping to 3.3V).
    *   **Outputs (x2)**: **1k** Series Resistor.

### Schematic / Wiring Logic

**Circuit Overview**:
```
   ┌─────────────────────────────────────────────────────────────────────────┐
   │                          RASPBERRY PI PICO                              │
   │                                                                         │
   │   ┌────────────────────────────────────────────────────────────────┐   │
   │   │                    The "Piano" UI                              │   │
   │   │   [C][C#][D][D#][E][F][F#][G][G#][A][A#][B]  ◄── 12 Buttons    │   │
   │   │   (●)(●)(●)(●)(●)(●)(●)(●)(●)(●)(●)(●)      ◄── 12 NeoPixels  │   │
   │   │                                                                │   │
   │   │   Buttons: GP10-GP21 (Internal PULL_DOWN)                      │   │
   │   │   LEDs: GP22 (Data) → Daisy chain                              │   │
   │   └────────────────────────────────────────────────────────────────┘   │
   │                                                                         │
   │   ┌──────────────────────────┐    ┌─────────────────────────────────┐  │
   │   │  CV IN A (Protected)     │    │  CV OUT A                       │  │
   │   │  [Jack]→[100k]→[GP26]    │──► │  (DAC 0x60) → [1k] → [Jack]     │◄─│
   │   │         │                │    │                                 │  │
   │   │      [Diode]→3.3V        │    └─────────────────────────────────┘  │
   │   └──────────────────────────┘                                         │
   │                                                                         │
   │   ┌──────────────────────────┐    ┌─────────────────────────────────┐  │
   │   │  CV IN B (Protected)     │    │  CV OUT B                       │  │
   │   │  [Jack]→[100k]→[GP27]    │──► │  (DAC 0x61) → [1k] → [Jack]     │◄─│
   │   │         │                │    │                                 │  │
   │   │      [Diode]→3.3V        │    └─────────────────────────────────┘  │
   │   └──────────────────────────┘                                         │
   └─────────────────────────────────────────────────────────────────────────┘
```

#### 2. Analog Front End (Standard Protection)
Replaces the old Op-Amp buffer with the simpler, safer "Bumblebee Standard":
```
   [CV IN Jack] ──► [100k Resistor] ──┬──► [Pico GP26/27]
                                      │
                                   [1N5817 Schottky]
                                      │
                                     3.3V (Pico Pin 36)
```
*   **Logic**: The 100k resistor limits current. If input > 3.3V, the diode conducts excess voltage to the 3.3V rail (safely).
*   **Calibration**: The Pico reads a scaled voltage. You MUST run the calibration script to map "1V" input to "Note C1".

#### 3. Power & DAC
*   **Power**: +12V from Rack -> L7805 -> Pico VSYS.
    *   **Add 10uF Capacitor** between +12V and GND near the regulator.
*   **DACs**: 1k resistor between DAC Output and Jack Tip.

### Step By Step guide

#### Phase 1: Power & DAC
1.  Solder Pico and L7805. Verify 5V and 3.3V rails.
2.  Connect MCP4725 to Pico (3.3V, GND, SDA, SCL).
3.  Run an I2C Scan script to verify connection (`address 0x60`).

#### Phase 2: Input Scaling
1.  Build the voltage divider + TL072 follower circuit on breadboard.
2.  Inject 10V from bench supply. Measure output at Pico ADC pin. It MUST NOT exceed 3.3V. Adjust resistor values if needed.
3.  Solder to main board.

#### Phase 3: Panel Integration
1.  Mount Pots/Jacks/LEDs to panel.
2.  Wire to main board.

### Phase 4: Verification & Calibration (CRITICAL)
1.  **Output Calibration (DAC)**:
    *   Power up the module.
    *   Write a simple MicroPython script to output `2048` (Mid-point) to the DACs.
    *   Measure the voltage at Jack A and Jack B with your multimeter.
    *   *Math*: The theoretical voltage is roughly 2.5V (Logic Level 3.3V / 4096 * 2048? No, MCP4725 uses VCC as ref).
    *   **Goal**: Ensure your code knows *exactly* what digital value creates **1.000V** (C1), **2.000V** (C2), etc.
    *   *Procedure*:
        *   Send values until you read exactly 1.00V on your meter. Note the value (e.g., `1220`).
        *   Send values until you read 4.00V. Note the value (e.g., `3650`).
        *   Update your `main.py` with these calibration points to ensure perfect tuning.

2.  **Input Calibration (ADC)**:
    *   Inject exactly 1.00V (using a trusted source or your own calibrated DAC output) into Input A.
    *   Read the ADC raw value in MicroPython.
    *   Inject 5.00V. Read raw value.
    *   Update your input scaling math to match these readings.

### Troubleshooting
*   **No Output**: Check I2C pullup resistors. The module usually has them, but check.
*   **Wrong Pitch**: The 0-3.3V range vs 0-10V range mapping is math-heavy. DO NOT SKIP STEP 4 (Calibration).
*   **LEDs reversed?**: Did you wire the zig-zag correctly? If C lights up when you press C#, your code array map is inverted relative to your wiring. Toggle `active_notes` in software to debug.
