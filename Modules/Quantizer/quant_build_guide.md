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
*   **Op-Amp**: **1x** TL072 (Dual Op-Amp) for Input Scaling.
    *   **1x** 8-pin IC Socket.
*   **User Input**:
    *   **12x** Tactile Buttons (6x6mm).
    *   **12x** PL9823 (or APA106) 5mm RGB LEDs (Through-hole NeoPixels).
*   **Jacks**: **4x** Thonkiconn PJ-301M-12 (CV In A, CV In B, CV Out A, CV Out B).
*   **Power**: **1x** L7805 CV (5V Regulator).
*   **Resistors (Input Scaling)**:
    *   **2x** 100k, **2x** 47k (Voltage Dividers).
    *   **2x** Schottky Diode (Input Protection).
*   **Protection (Outputs)**:
    *   **2x** 1k Resistors (Placed in series with Output Jacks to protect DACs).

### Schematic / Wiring Logic

#### 1. The Brain (Pico)
*   **I2C Bus (DACs)**:
    *   GP8 (SDA) -> Connect to SDA on BOTH DACs.
    *   GP9 (SCL) -> Connect to SCL on BOTH DACs.
    *   VCC -> 3.3V (or 5V if using level shifters, usually 3.3V is fine for MCP4725).
*   **The "Piano" (UI)**:
    *   **Buttons (Input)**: Connect 12 buttons to 12 GPIOs. (e.g., GP10 - GP21).
    *   **LEDs (Output)**: GP22 -> Data In of First LED. (Daisy chain Data Out -> Data In).
    *   **Physical Layout (CRITICAL)**: Do not place LEDs in a straight line.
        *   Place each LED **directly above** its corresponding button.
        *   Since "Black Key" buttons are offset higher than "White Key" buttons, their LEDs must also be offset higher.
        *   *Wiring Order*: Daisy-chain them chromatically (C -> C# -> D...) by zig-zagging the data wire. This keeps the software array logic simple (`0=C`, `1=C#`).
*   **Analog Inputs**:
    *   **CV In A** -> Scaled -> GP26 (ADC0).
    *   **CV In B** -> Scaled -> GP27 (ADC1).
*   **Power**:
    *   Pico VSYS <- +5V from L7805.
    *   Pico GND <- Common Ground.

#### 2. Analog Front End (Dual Channel)
*   **CV Input Scaling (Repeat twice)**:
    *   **Divider**: Input -> 100k -> [Point A] -> 49.9k (or 47k+trim) -> GND.
    *   **Buffer**: [Point A] -> TL072 Input (+).
    *   **Output**: TL072 Output -> Pico ADC Pin.
    *   *Goal*: 10V input = ~3.2V at ADC.

#### 3. Wiring Summary
*   **Panel PCB (Stripboard?)**:
    *   Holds 12 Buttons + 12 PL9823 LEDs.
    *   Connects to Main Board via ribbon cable (12 Button lines + 1 LED Data + 5V + GND).
*   **Main Board**: Pico, Power, DACs, Op-Amps.

#### 4. DAC Configuration
*   **DAC 1**: Address 0x60 (Default). VOUT -> 1k Resistor -> Jack A Tip.
*   **DAC 2**: Address 0x61 (Bridged A0). VOUT -> 1k Resistor -> Jack B Tip.
*   *Note*: The 1k resistor is critical. It protects the DAC if you accidentally patch an Input signal into the Output jack.

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
