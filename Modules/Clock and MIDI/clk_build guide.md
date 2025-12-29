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
*   **Jacks**: **5x** Thonkiconn PJ-301M-12.
*   **Power**:
    *   **1x** L7805 CV (5V Regulator).
    *   **1x** 10uF Electrolytic Capacitor (Power bypass).
    *   **1x** 10-pin Eurorack Power Header.
*   **Protection (Standard Bumblebee Protocols)**:
    *   **Input (Clock In)**: **1x 100k** Series Resistor + **1N5817** Schottky Diode (Clamping to 3.3V).
    *   **Outputs (x4)**: **1k** Series Resistor (After Buffer).

### Schematic / Wiring Logic

**Circuit Overview**:
```
   ┌─────────────────────────────────────────────────────────────────────────┐
   │                          RASPBERRY PI PICO                              │
   │                                                                         │
   │  ┌──────────────┐   ┌──────────────────────────────────────────────┐   │
   │  │   I2C LCD    │   │              GPIO MAPPING                    │   │
   │  │   (2004)     │   │                                              │   │
   │  │   GP0/GP1    │   │  ADC Inputs (Pots)         Digital Outputs   │   │
   │  └──────────────┘   │  ├── GP26: Master Knob     ├── GP2-5: Clocks │   │
   │                     │  ├── GP27: Chan Knob       ├── GP13-15: LEDs │   │
   │  ┌──────────────┐   │  └── GP28: Opt Knob        └── GP6-8: LEDs   │   │
   │  │   CLOCK IN   │   │                                              │   │
   │  │ (Protected)  │   │  Digital Inputs                              │   │
   │  └──────────────┘   │  ├── GP9: Clock In (protected)               │   │
   │                     │  ├── GP10-12: Encoder                        │   │
   │  ┌──────────────┐   │  ├── GP16: Chan Button                       │   │
   │  │   CD4050     │   │  └── GP17: Opt Button                        │   │
   │  │   (Buffer)   │   └──────────────────────────────────────────────┘   │
   │  │ 3.3V → 5V    │                                                       │
   │  └──────────────┘                                                       │
   └─────────────────────────────────────────────────────────────────────────┘
             │
             ▼
   ┌────────────────────────────────────────────────────────┐
   │     CLOCK OUTPUTS (via CD4050 buffer + 1k resistor)    │
   │   Out 1   Out 2   Out 3   Out 4                        │
   └────────────────────────────────────────────────────────┘
```

#### GPIO Pin Assignment

> **Note**: ADC pins (GP26-28) are analog inputs only and cannot drive LEDs. All LEDs use standard digital GPIOs.

| Function | GPIO | Notes |
|----------|------|-------|
| **I2C (LCD)** | | |
| SDA | GP0 | |
| SCL | GP1 | |
| **ADC (Knobs)** | | |
| Master Knob | GP26 | ADC0 |
| Channel Knob | GP27 | ADC1 |
| Option Knob | GP28 | ADC2 |
| **Digital Inputs** | | |
| Clock In | GP9 | Protected: 100k + Schottky |
| Channel Button | GP16 | PULL_DOWN |
| Option Button | GP17 | PULL_DOWN |
| Encoder A/B/Sw | GP10-12 | |
| **Digital Outputs** | | |
| Clock Out 1-4 | GP2-5 | Via CD4050 buffer |
| Channel LEDs | GP13-15 | Out 2/3/4 indicators |
| Option LEDs | GP6-8 | Swing/Euclid/Jitter |

#### Input Protection (Clock In)
```
   [Jack Tip]──►[100k Resistor]──┬──►[GP9]
                                 │
                                 └──►[1N5817]──►3.3V
```
Protects against over-voltage from 5V gates.

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
