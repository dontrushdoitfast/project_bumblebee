# Simple Dirty Delay Build Guide

### Overview
This build combines an Op-Amp (Analog) with the PT2399 (Digital) and requires an onboard voltage regulator. Single channel keeps complexity manageable.

### Tools needed
*   **Soldering Iron** & Solder
*   **Multimeter**
*   **Track Cutter**
*   **Wire Strippers**

### Bill Of Materials
*   **Chips**:
    *   **1x** PT2399 (Echo Processor) + 16-pin Socket.
    *   **1x** TL072 (Op-Amp) + 8-pin Socket.
    *   **1x** L78L05 (5V Regulator - TO-92 package).
*   **Controls**:
    *   **3x** B50k or B100k Pots (16mm Panel Mount).
    *   **2x** 3.5mm Mono Jacks (Panel Mount).
*   **Power**:
    *   **1x** 10-pin Male Header.
*   **Passives**:
    *   **Resistors**: 10k (x2), 15k (x1), 22k (x1), 1k (x1 output protection).
    *   **Capacitors**: 100nF Ceramic (x2), 47uF Electrolytic (x1), 2.2uF Electrolytic (x1).
    *   *Note*: See PT2399 datasheet for exact anti-aliasing capacitor values.
*   **Power**:
    *   **1x** 10-pin Eurorack Header.

### Schematic / Wiring Diagram
```
              ┌────────────────┐
   +12V ──────┤ L78L05         ├──────► +5V (to PT2399)
              │  IN  GND  OUT  │
              └───────┬────────┘
                      │
                     GND

   ┌─────────────────────────────────────────────────────────────┐
   │                       SIGNAL PATH                           │
   │                                                             │
   │  [IN JACK]──►[TL072 Buffer]──►┌──────────────┐              │
   │                               │   PT2399     │              │
   │                   Feedback◄───┤   (5V only)  ├───►[Wet]     │
   │                   Pot         └──────────────┘      │       │
   │                        Time Pot──►Pin 6             │       │
   │                                                     ▼       │
   │  [Dry]────────────────────────────────────►[Mix Pot]        │
   │                                                 │           │
   │                                      [TL072 Output Buffer]  │
   │                                                 │           │
   │                                            [OUT JACK]       │
   └─────────────────────────────────────────────────────────────┘
```

### Step By Step guide

#### Phase 1: Breadboard (Single Channel)
1.  **Power**: Setup +12V/-12V. **Add L78L05**. Verify you have stable +5V. **Do not feed 12V to the PT2399!**
2.  **IC**: Place PT2399. Power Pin 1 (+5V) and Pins 3/4 (Ground).
3.  **Logic**: Connect the "Time" resistor (Pin 6) and "Feedback" path.
4.  **Audio**: Inject audio. Do you hear echoes?

#### Phase 2: Stripboard Layout
1.  **Planning**: Fit 2 chips (PT2399, TL072). Medium stripboard (approx 15x20 holes).
2.  **Isolation**: Locate the L78L05 away from the audio path to minimize heat/noise.
3.  **Grounding**: Create solid ground connections as digital chips are noisy.

#### Phase 3: Panel Wiring
1.  **Mount**: 3 Pots + 2 Jacks fits comfortably in 4HP.
2.  **Wire**: Standard pot wiring.
    *   **Time Pot**: Variable resistance to Ground from Pin 6.
    *   **Feedback Pot**: Simple attenuator in the feedback loop.

### Troubleshooting
*   **PT2399 Gets Hot**: You fed it 12V. It is dead. Replace it.
*   **Lock up (Screaming noise on startup)**: Add a proper power-on reset circuit (small capacitor on the digital ground pin).
*   **Distortion**: Input signal is too hot. The PT2399 clips easily at modular levels. Attenuate before the chip.

### Testing plan
1.  **Voltage Check**: Verify **Pin 1 of PT2399 is +5V**. If it's 12V, stop.
2.  **Audio Path**: Dry signal passes cleanly?
3.  **Delay**: Turn Mix to Wet. Turn Time. Do pitch shifting artifacts happen? (Good, that's the "Dirty" part).
