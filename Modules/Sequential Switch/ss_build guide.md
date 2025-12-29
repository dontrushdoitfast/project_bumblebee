# Sequential Switch Build Guide

### Overview
This module introduces **Active Electronics** (Integrated Circuits). You will wire a logic chip (4017) to talk to an analog switch (4051). Precision is key here; a single misplaced wire on the breadboard means it won't work.

### Tools needed
*   **Soldering Iron**, Solder, Cutters, Strippers.
*   **Multimeter** (Logic debugging: 0V vs 5V).
*   **Breadboard** (Essential for logic validation).

### Bill Of Materials
Note: we want 2 of these. So double the parts below.

*   **ICs**:
    *   **1x** CD4017BE (Decade Counter).
    *   **1x** CD4051BE (8-Channel Analog Mux/Demux).
*   **Jacks**:
    *   **7x** Thonkiconn PJ-301M-12 (Clock, Reset, Common, 4x Steps).
*   **LEDs**:
    *   **4x** 3mm LEDs (Color of choice).
    *   **4x** 1k Resistors (Current limiting).
*   **Logic Helpers**:
    *   **1x** 2N3904 NPN Transistor (Buffer for Clock input).
    *   **1x** 100k Resistor (Pull-down for Clock).
    *   **1x** 1N4148 Diode (Protection).

### Schematic / Wiring Diagram
**Logic Details**:
1.  **Clock Circuit**: Jack -> Transistor Buffer -> CD4017 CLK (Pin 14).
2.  **Reset Logic**: CD4017 Reset (Pin 15) connected to **Step 5 Output (Pin 10)**. This forces it to reset to Step 1 immediately after Step 4, creating a 4-step loop.
3.  **Address Translation**:
    *   This is the tricky part. The 4017 outputs "One Hot" (individual pins go high). The 4051 expects "Binary" (A/B/C pins).
    *   *Simplification*: Actually, for a pure 4-step, using a **CD4066** (Quad Switch) might be easier logic-wise, BUT the **CD4051** is better for audio.
    *   *Correction*: To drive the 4051 Address pins (A, B) from the 4017, we need diode OR logic OR simply use the 4017 outputs to drive **CD4066** control pins.
    *   **REVISED DESIGN**: For simplicity and robustness (the "Basic Electronics" goal), we will use **CD4017 outputs driving 4 sections of a CD4066**.
    *   *Wait*: CD4066 clips audio on single supply. To pass +/- audio, CD4066 needs special biasing OR use the CD4051.
    *   *Final Decision*: **Clock -> 2-bit Binary Counter (CD4520) -> CD4051 Address Pins**. This is cleaner.
    *   *Alternative (Simpler)*: **CD4017 Output 0 -> drive LED & Switch Control??** No.
    *   *Best for Beginner*: **CD4017 -> Diode Logic -> CD4051 Address Inputs**.
        *   Step 0 (00): A=0, B=0
        *   Step 1 (01): A=1, B=0
        *   Step 2 (10): A=0, B=1
        *   Step 3 (11): A=1, B=1
        *   *Implementation*: Connect 4017 outputs to A/B lines via 1N4148 diodes.

**Pinout Summary (CD4051)**:
*   VEE (Pin 7): -12V (Critical for bi-polar audio!)
*   VSS (Pin 8): Ground
*   VDD (Pin 16): +12V

### Step By Step guide

#### Phase 1: Breadboard Logic Check
1.  **Power**: Put CD4017 and CD4051 on board. Power them (+12V/GND, and -12V to 4051 VEE).
2.  **Clock**: Setup the Clock input to step the 4017. Verify with LEDs on 4017 outputs 0-3.
3.  **Reset**: Wire 4017 Pin 10 (Output 4) to Pin 15 (Reset). Verify it loops 4 steps.
4.  **Audio**: Inject Audio into CD4051 Common. Connect Scope/Amp to Output 0.
5.  **Link**: Connect Logic (4017) to Switch (4051) using the Diode Logic method.
6.  **Verify**: Does Audio move from Out 0 -> Out 1 -> Out 2 -> Out 3?

#### Phase 2: Stripboard
*(User to follow standard "Baby 8" or "4-Step Sequencer" stripboard layouts available online, verifying pinouts against datasheets).*

### Troubleshooting
*   **Skips Steps**: Clock signal is noisy. Add a Schmitt Trigger or capacitor to filter input.
*   **Audio Distorts**: Check CD4051 VEE pin. If it's at Ground, negative signals clip. It MUST be at -12V.
*   **Stuck on Step 1**: Reset pin is floating high. Ensure it has a pull-down resistor if using an external reset jack.

### Testing plan
1.  **LED Chase**: Do the lights move?
2.  **Bidirectional Test**: 
    -   Mux Mode: 4 different oscillators in -> 1 output. Does the timbre change every step?
    -   Demux Mode: 1 LFO in -> 4 outputs. Patch outputs to 4 different filter cutoffs. Does the filter dance?
