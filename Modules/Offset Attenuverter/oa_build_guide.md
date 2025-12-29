# Offset / Attenuverter Build Guide

### Overview
This build creates a simple but useful op-amp circuit. It mixes an input signal with a fixed voltage (Offset) and allows you to scale that input signal positively or negatively (Attenuverter).

### Tools needed
*   **Soldering Iron** & Solder
*   **Multimeter**
*   **Track Cutter** (or drill bit)
*   **Wire Strippers**

### Bill Of Materials
*   **1x** Stripboard.
*   **1x** TL072 Dual Op-Amp (or TL074 Quad if building dual version).
*   **1x** 8-pin IC Socket (for TL072).
*   **2x** B100K Potentiometers (Linear). *Note: Center detent is nice for the Attenuverter but not essential.*
*   **Jacks**:
    *   **2x** PJ-301M-12 (3.5mm Eurorack Jacks).
*   **Resistors (1/4W)**:
    *   **3x** 100k (Input/Feedback resistors for Unit Gain).
    *   **2x** 1k (Output protection and LED current limiting).
*   **Capacitors**:
    *   **2x** 100nF Ceramic (Power decoupling).
    *   **2x** 10uF Electrolytic (Power filtering).
*   **Indicators**:
    *   **1x** Bipolar LED (or two standard LEDs back-to-back).
*   **Power**:
    *   **1x** 10-pin Eurorack Power Header.

### Schematic / Wiring Diagram
**Logic**:
1.  **Stage 1 (Attenuverter)**:
    *   The input signal goes to a potentiometer.
    *   The wiper of the pot feeds the Op-Amp logic to fade between Inverted and Non-Inverted signal. *Common design: "Crossfader" implementation.*
2.  **Stage 2 (Offset & Summer)**:
    *   The "Offset" pot acts as a voltage divider between +12V and -12V.
    *   The output of Stage 1 and the Offset voltage are summed together in the second Op-Amp stage.
3.  **Output**:
    *   The result is sent to the Output jack via a 1k protection resistor.
    *   An LED monitors the final voltage.

### Step By Step guide

#### Phase 1: Breadboard Prototyping
1.  Set up your breadboard with +/- 12V.
2.  Place the TL072. Connect Power (Pin 8 = +12V, Pin 4 = -12V).
3.  Build the Offset section first: One Op-amp configured as a voltage follower or summer for the pot wiper. Check it swings +/- 10V (approx).
4.  Add the Input stage. Verify you can invert a signal (use an LFO or steady DC voltage to test).

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
