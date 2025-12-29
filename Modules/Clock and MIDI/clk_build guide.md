# Clock Generator Build Guide

### Overview
This build features a "Modal" interface. You will be wiring up buttons and LEDs to create a "Select + Edit" workflow. This reduces the number of expensive pots needed while increasing functionality.

### Tools needed
*   **Soldering Iron**
*   **Computer** (MicroPython)
*   **Wire Strippers**

### Bill Of Materials
*   **Microcontroller**: **1x** Raspberry Pi Pico.
*   **Logic Buffer**: **1x** CD4050BE (Hex Buffer) or 74HC245. + Socket.
*   **Screen**: **1x** LCD 2004 (20x4) with I2C Backpack.
*   **User Input**:
    *   **1x** Rotary Encoder (with Push Switch).
    *   **3x** B10k or B100k Potentiometers (Linear).
    *   **2x** Momentary Push Buttons (Tactile or Panel mount).
    *   **3x** Knobs for Pots.
*   **Indicators**:
    *   **6x** 3mm LEDs (3x Green for Channels, 3x Red for Options).
    *   **6x** 1k Resistors (Current limiting).
*   **Jacks**: **5x** Thonkiconn PJ-301M-12.
*   **Power**: **1x** L7805 CV (5V Regulator).
*   **Protection (Critical)**:
    *   **1x** 1k Resistor (Series).
    *   **1x** 3.3V Zener Diode (Shunt to Ground) OR **2x** Schottky Diodes (Rail clamping). *Goal: Cap input voltage at 3.3V.*

### Schematic / Wiring Logic

#### 1. The Brain (Pico)
*   **I2C Bus (Screen)**: GP0 (SDA), GP1 (SCL).
*   **Common Controls**:
    *   **Encoder**: GP10, GP11 (A/B), GP12 (Sw).
    *   **Master Knob**: GP26 (ADC0).
*   **Section A (Channels)**:
    *   **Button**: GP16 (Pull Down).
    *   **Knob**: GP27 (ADC1).
    *   **LEDs**: GP13 (Out 2), GP14 (Out 3), GP15 (Out 4).
*   **Section B (Options)**:
    *   **Button**: GP17 (Pull Down).
    *   **Knob**: GP28 (ADC2).
    *   **LEDs**: GP22 (Swing), GP26 (Euclid), GP27 (Jitter) -> *Wait, ADC pins can't drive LEDs easily while reading pots?*
    *   *Correction*: **ADC pins (GP26-28) are Analog INPUTS only.** We cannot use them for LEDs.
    *   *Revised LED Mapping*:
        *   **Option LEDs**: GP6, GP7, GP8.

#### 2. Wiring Summary (Revised)
*   **Inputs (ADC)**:
    *   Master Knob -> GP26
    *   Chan Knob -> GP27
    *   Opt Knob -> GP28
*   **Inputs (Digital)**:
    *   Chan Button -> GP16
    *   Opt Button -> GP17
    *   Encoder -> GP10, 11, 12.
    *   **Clock In (Protected)**:
        *   Jack Tip -> 1k Resistor -> Pico GP9.
        *   *AND* Pico GP9 -> Cathode (Line) of 3.3V Zener -> Ground.
        *   *Result*: If >3.3V enters, Zener dumps excess to ground. If <0V enters, Zener block/conducts based on type. *Ideally use BAT54S clamping for full protection, but Zener + Resistor is decent for 5V gates.*
*   **Outputs (Digital)**:
    *   **Clock Jacks** (via Buffer):
        *   GP2 -> Out 1
        *   GP3 -> Out 2
        *   GP4 -> Out 3
        *   GP5 -> Out 4
    *   **LEDs**:
        *   Chan LEDs: GP13, GP14, GP15
        *   Opt LEDs: GP6, GP7, GP8

### Step By Step guide

#### Strategy: Daughterboard Design
Because this module has **17 Panel Components** (Screen, 3 Pots, 3 Knobs, 2 Buttons, 6 LEDs, 5 Jacks), wiring them all individually to one main board is a mess.
*   **Main Board**: Holds Pico, CD4050, Power, Input Protection. Mounted deeper in the case.
*   **Panel**: Mount pots/buttons/LEDs/Screen to the 3D Printed Faceplate.
*   **Connection**: Use **Ribbon Cables** or solid core wire bundles to connect Panel Components to Main Board.
    *   *Bundle 1*: I2C (4 wires) for Screen.
    *   *Bundle 2*: Controls (Pots/Buttons/Encoder).
    *   *Bundle 3*: LEDs.

#### Phase 1: LED & Button Logic
1.  Wire the 6 LEDs and 2 Buttons to the Pico on a breadboard.
2.  Write a simple script: `if button_a.value(): led_1.toggle()`.
3.  Ensure you can cleanly cycle through the 3 states (LED 1 -> LED 2 -> LED 3) with each button press.

#### Phase 2: Potentiometer Latching
*   *Software Concept*: Since one knob controls 3 different things, the value shouldn't "Jump" when you switch channels.
*   *Solution*: The code must implement "Pass-Through" or "Catch-Up" logic. The value only changes when the physical knob crosses the stored digital value.

#### Phase 3: Buffer & Output
1.  Wire the Pico GP2-5 pins to the CD4050 Inputs.
2.  Wire CD4050 Outputs to the Jacks.
3.  **Test**: Set Out 1 to Master. Scope it. It should be a clean 0V-5V square wave.

### Troubleshooting
*   **Ghost Button Presses**: Digital inputs need Pull-Down resistors. Use `Pin(X, Pin.IN, Pin.PULL_DOWN)` in code, or add physical 10k resistors to ground.
*   **Jittery Values**: ADC readings fluctuate. Use a software smoothing filter or "hysteresis" to stop the clock division from flickering between "/4" and "/3".

### Testing plan
1.  **UI Stress Test**: Rapidly click through channels while turning the knob. Ensure the screen updates correctly and the LEDs follow.
2.  **Euclid Check**: Select "Option > Euclid". Turn knob. Does Out 4 start skipping beats rhythmically?
