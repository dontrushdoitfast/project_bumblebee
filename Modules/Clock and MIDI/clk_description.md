# Clock Generator Description and Requirements

### Description
The **Clock Generator** is a "Smart Lab" timing module. It uses a **Select + Edit** workflow to pack advanced functionality into a clean interface.
Instead of menu diving, you press a button to select a target (e.g., Output 2), and an LED lights up to tell you *exactly* what the knob is currently controlling.

### Requirements
1.  **Core Function**: 4-Channel Clock Source.
    *   **Out 1**: Master Clock (Always active).
    *   **Outs 2-4**: Configurable Multipliers/Dividers.
2.  **Advanced Features**:
    *   **Swing**: Global groove control (affects all outputs).
    *   **Jitter**: Humanization / Slop.
    *   **Euclidean Generator**: Turns **Output 4** into a rhythmic gate sequencer.
3.  **Interface**:
    *   **Master Knob**: Instant BPM control.
    *   **Channel Editor**: Selects Out 2, 3, or 4 -> Edits Div/Mult Ratio.
    *   **Option Editor**: Selects Swing, Euclidean, or Jitter -> Edits Amount.

### Panel Layout / Interface
*   **Top**: 2004 LCD Screen (Visualizing BPM and States).
*   **Controls**:
    *   **Master Knob** (Top Left).
    *   **Section A (Channel Select)**:
        *   1x Push Button (Cycles Selection).
        *   3x LEDs (Indicate Out 2 / Out 3 / Out 4).
        *   1x Knob (Edits Value).
    *   **Section B (Option Select)**:
        *   1x Push Button (Cycles Selection).
        *   3x LEDs (Indicate Swing / Euclid / Jitter).
        *   1x Knob (Edits Value).
        *   **Reset**: Hold Button for 3 seconds -> Resets Swing, Euclid, and Jitter to 0.
    *   **Bottom**: Jacks (Clock In, Out 1, Out 2, Out 3, Out 4).

### Technical Specifications
*   **Core**: Raspberry Pi Pico (RP2040).
*   **Output Voltage**: **+5V** Pulses (Buffered via CD4050/74HC245).
*   **User Input**:
    *   **Potentiometers**: 3x (Master, Edit A, Edit B).
    *   **Buttons**: 2x Tactile (Select A, Select B).
    *   **Encoder**: 1x (Menu Navigation/Global settings).

### Exclusions
*   **Euclidean on All Channels**: To keep the interface simple, Euclidean rhythms are exclusive to **Output 4**. Outs 1-3 are strict Clocks/Dividers.
