# Dual Offset / Attenuverter Build Guide

### Overview
This build creates a simple but useful op-amp circuit. It mixes an input signal with a fixed voltage (Offset) and allows you to scale that input signal positively or negatively (Attenuverter).

### Tools needed
*   **Soldering Iron** & Solder
*   **Multimeter**
*   **Track Cutter** (or drill bit)
*   **Wire Strippers**

### Bill Of Materials
**Note**: We want 2 of these, so double it.

*   **1x** Stripboard (Large enough for TL074 layout).
*   **1x** **TL074** Quad Op-Amp (DIP-14).
*   **1x** **DIP-14 Socket**.
*   **4x** B100K Potentiometers (Linear).
*   **4x** Knobs (Davies 1900 Clone).
*   **Jacks**:
    *   **4x** Thonkiconn PJ-301M-12.
*   **Resistors (1/4W Metal Film)**:
    *   **6x** 100k (3 per channel: Input buffer, Summer in, Feedback).
    *   **4x** 1k (Output protection, LED current).
*   **Capacitors**:
    *   **2x** 100nF Ceramic.
    *   **2x** 10uF Electrolytic.
*   **Indicators**:
    *   **2x** Bipolar LEDs (One per channel).
*   **Power**:
    *   **1x** 10-pin Eurorack Power Header.

### Schematic / Wiring Diagram
**Logic**:
1.  **Stage 1 (Attenuverter)**:
    *   The input signal goes to a potentiometer.
    *   The wiper of the pot feeds the Op-Amp logic to fade between Inverted and Non-Inverted signal.
2.  **Stage 2 (Offset & Summer)**:
    *   The "Offset" pot acts as a voltage divider between +12V and -12V.
    *   The output of Stage 1 and the Offset voltage are summed together in the second Op-Amp stage.
3.  **Output**:
    *   The result is sent to the Output jack via a 1k protection resistor.
    *   An LED monitors the final voltage.

**Circuit Diagram (Per Channel)**:
```
                    ATTENUVERTER                        OFFSET + SUMMER
   ┌──────────────────────────────┐    ┌──────────────────────────────────────┐
   │                              │    │                                      │
   │  [IN]──►┌───────┐            │    │   +12V                               │
   │         │  POT  │            │    │    │                                 │
   │         │ (Att) ├──►[Op-Amp]─┼────┼───►├──►[Op-Amp Summer]──►[1k]──►[OUT]│
   │         │       │   Inverter │    │    │      ▲                          │
   │         └───────┘            │    │  [POT]    │                          │
   │              ▲               │    │ (Offset)  │                          │
   │       Crossfader             │    │    │      │                          │
   │       wiring                 │    │   -12V    │                          │
   └──────────────────────────────┘    └───────────┴──────────────────────────┘
                                                 (Offset voltage added)
```

### Step By Step guide

#### Phase 1: Breadboard Prototyping
1.  Set up your breadboard with +/- 12V.
2.  Place the TL072. Connect Power (Pin 8 = +12V, Pin 4 = -12V).
3.  Build the Offset section first: One Op-amp configured as a voltage follower or summer for the pot wiper. Check it swings +/- 10V (approx).
4.  Add the Input stage. Verify you can invert a signal.
5.  **Repeat**: Build the second channel on the breadboard to verify the TL074 pinout (14 pins is busier than 8!).

#### Phase 2: Stripboard Assembly
1.  **Layout**: Plan your stripboard. Ensure the IC is centrally located.
2.  **Cuts**: Cut tracks under the IC.
3.  **Links**: Add ground and power links.
4.  **Components**: Resistors -> Sockets -> Capacitors.
5.  **Wiring**: Solder leads for the Pots and Jacks (about 10cm length).

#### Phase 3: Panel Wiring
1.  Mount Pots and Jacks to the 3D printed faceplate.
2.  Solder wires to the components:
    *   **Pots**: Pin 1 to -12V/Inverted, Pin 3 to +12V/Non-Inverted (depending on circuit choice).
    *   **Jacks**: Tip to board, Sleeve to Ground.
3.  Connect the LED (verify polarity by testing!).

### Troubleshooting
*   **Offset doesn't center**: Check if your pot is Linear (B) or Logarithmic (A). Linear is required here.
*   **Signal is clipped**: You might be exceeding the headroom of the TL072 (approx +/- 10.5V). This is normal.
*   **Oscillation / Noise**: Ensure unused Op-Amp inputs (if any) are grounded or add more 100nF decoupling capacitors near the power pins.

### Testing plan
1.  **Smoke Test**: Check for shorts before plugging in.
2.  **Null Test**: Set both knobs to center. Input 0V (nothing). Output should be ~0V.
3.  **Offset Check**: Turn Offset knob. Output should swing form approx -10V to +10V.
4.  **Attenuvert Check**: Patch a steady positive voltage (e.g. +5V). 
    *   Turn Attenuverter CW: Output increases positive.
    *   Turn Attenuverter CCW: Output becomes negative (Inverted).
