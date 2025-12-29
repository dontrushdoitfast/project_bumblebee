# CV Mixer Build Guide

### Overview
This is an active module build, meaning it requires power and uses an Integrated Circuit (IC). We will use a TL072 Op-Amp to create a "Summing Amplifier". This ensures that mixing one channel doesn't drop the volume of the others. We will use a small piece of stripboard or "dead-bug" wiring style for the circuit.

### Tools needed
*   **Soldering Iron** & Solder
*   **Wire Strippers** & Cutters
*   **Multimeter**
*   **Breadboard** (highly recommended for testing Op-Amp orientation)
*   **3D Printer** (Creality K1 Max)

### Bill Of Materials
*   **1x** **TL072** Dual Op-Amp (DIP-8 package).
*   **1x** **DIP-8 Socket** (Optional but recommended to protect the IC).
*   **4x** **Thonkiconn PJ-301M-12** (3.5mm Mono Jacks).
*   **3x** **Alpha 9mm Vertical Potentiometer, B100K** (Linear).
*   **3x** **Knobs** (Davies 1900 Clone).
*   **5x** **100k Resistors** (1/4W Metal Film).
    *   3x for Inputs
    *   1x for Feedback (Stage 1)
    *   1x for Feedback (Stage 2)
*   **1x** **1k Resistor** (Output protection).
*   **2x** **100nF Ceramic Capacitors** (Power decoupling).
*   **1x** **10-pin Eurorack Power Header** (or hardwired cable).
*   **Stripboard** (Small piece, approx 10x10 holes).

### Schematic / Circuit Logic
The circuit has two stages using the two halves of the TL072:
1.  **Stage 1 (Summing)**: Inputs are reduced by the pots, then go through 100k resistors to the *Inverting Input (-)* of Op-Amp A. The feedback resistor is also 100k, creating Unity Gain. The output is inverted (Negative).
2.  **Stage 2 (Inverting)**: The output of Stage 1 goes to the *Inverting Input (-)* of Op-Amp B through a 100k resistor. Feedback is 100k. This re-inverts the signal, making it Positive (In Phase) again.

**Power Connections**:
*   TL072 Pin 8 -> +12V
*   TL072 Pin 4 -> -12V
*   (Add 100nF capacitors from each power pin to Ground for stability).

### Step By Step guide

#### Phase 1: Breadboard Prototyping
1.  **Power**: Connect +/-12V from your power supply (or bench supply) to the breadboard rails.
2.  **IC**: Insert TL072. Connect Pin 8 to +12V, Pin 4 to -12V.
3.  **Basic Mix check**:
    *   Connect two audio sources to the breadboard.
    *   Run them through 100k resistors to Pin 2 (Inverting Input A).
    *   Connect 100k Feedback resistor from Pin 1 (Output A) to Pin 2.
    *   Ground Pin 3 (Non-Inverting Input A).
    *   Buffer Stage: Connect Pin 1 to Pin 6 (Inverting Input B) via 100k. 100k Feedback Pin 7 to 6. Ground Pin 5.
    *   Listen to Pin 7 (Output B). You should hear both signals mixed cleanly.

#### Phase 2: Assembly
1.  **Faceplate**: Print the 6HP faceplate.
2.  **Mount Hardware**: Install Potentiometers and Jacks.
3.  **Circuit Board**:
    *   Solder the IC socket and resistors onto the small stripboard strip.
    *   Cut traces under the IC to prevent shorts!
4.  **Wiring**:
    *   **Inputs**: Jack Tips -> Pot Pin 3. Pot Pin 2 (Wiper) -> 100k Resistor -> PCB Summing Point.
    *   **Output**: PCB Output -> 1k Resistor -> Output Jack Tip.
    *   **Grounds**: Common ground for all Jacks, Pots, and PCB.
    *   **Power**: Wired to the 10-pin header. **Double check polarity!** (-12V usually indicated by "Red Stripe").

#### Phase 3: Final Check
1.  **Smoke Test**: Check for shorts between +12V, -12V, and GND on the power connector before plugging in.
2.  **Voltage Check**: Power up without any inputs. Output DC voltage should be ~0V (might have slight offset <20mV).
3.  **Audio Test**: Mix two signals. Ensure knobs work smoothly from silence to full volume.

### Troubleshooting
*   **Distortion**: Check if signals are too hot (Eurorack levels can clip if Op-Amp gain is too high, but 100k:100k is unity, so it should be fine).
*   **Oscillation**: Ensure 100nF decoupling capacitors are close to the IC power pins.
*   **Inverted Phase**: If you skipped Stage 2, the output will be upside down (audibly identical for audio, but matters for CV).
