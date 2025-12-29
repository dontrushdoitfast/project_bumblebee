# Simple Dirty Delay Description and Requirements

### Description
The **Simple Dirty Delay** is a dual-channel lo-fi echo module based on the classic **PT2399** Echo processor. It provides gritty, digital repeats that degrade into noise at longer delay times. 
It is "Dirty" because:
1.  The PT2399 introduces digital aliasing and noise at slow speeds.
2.  The filtering is kept minimal to preserve character.
3.  It excels at karplus-strong synthesis, metallic reverbs, and dub-style degradation.

### Requirements
1.  **Capacity**: Two independent delay lines (Channel A / Channel B).
2.  **Core**: PT2399 Digital Echo IC.
3.  **Controls per Channel**:
    *   **Time**: Sets delay length (approx 30ms to 300ms).
    *   **Feedback**: Sets repeats (from 1 repeat to self-oscillation/noise wall).
    *   **Mix**: Blends between Dry (Input) and Wet (Delay).
4.  **Power**: Requires +12V/-12V. **Crucial**: Includes onboard 5V regulation (L78L05) because the PT2399 is a 5V chip.

### Panel Layout / Interface
*   **Width**: 8HP (To accommodate 6 knobs + 4 jacks).
*   **Controls**:
    *   **Top**: 3 Knobs for Channel A (Time, Feedback, Mix).
    *   **Middle**: Jacks (In A, Out A, In B, Out B).
    *   **Bottom**: 3 Knobs for Channel B.
*   **Layout Logic**: Channel A Top, Channel B Bottom. Compact but usable.

### Technical Specifications
*   **Delay Chip**: PT2399.
*   **Regulator**: L78L05 (Onboard +5V generation from +12V rail).
*   **Op-Amps**: TL072/TL074 for input buffering and output mixing.
*   **Delay Range**: Tuned for "Musical" range, but allows pushing into "Garbage" range (clock noise visible).

### Exclusions
*   **CV Control**: To keep it "Simple", there is NO Voltage Control over Time or Feedback in this version. Knobs only.
*   **Tap Tempo**: Not possible with the PT2399 logic.
