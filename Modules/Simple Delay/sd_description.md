# Simple Dirty Delay Description and Requirements

**Difficulty: ⭐⭐⭐ Intermediate** — *Combines analog and digital ICs. Requires onboard 5V regulation.*

### Description
The **Simple Dirty Delay** is a lo-fi echo module based on the classic **PT2399** Echo processor. It provides gritty, digital repeats that degrade into noise at longer delay times. 
It is "Dirty" because:
1.  The PT2399 introduces digital aliasing and noise at slow speeds.
2.  The filtering is kept minimal to preserve character.
3.  It excels at karplus-strong synthesis, metallic reverbs, and dub-style degradation.

### Requirements
1.  **Capacity**: Single delay line (keeps it simple!).
2.  **Core**: PT2399 Digital Echo IC.
3.  **Controls**:
    *   **Time**: Sets delay length (approx 30ms to 300ms).
    *   **Feedback**: Sets repeats (from 1 repeat to self-oscillation/noise wall).
    *   **Mix**: Blends between Dry (Input) and Wet (Delay).
4.  **Power**: Requires +12V/-12V. **Crucial**: Includes onboard 5V regulation (L78L05) because the PT2399 is a 5V chip.

### Panel Layout / Interface
*   **Width**: 4HP
*   **Controls**:
    *   **Top**: 3 Knobs (Time, Feedback, Mix).
    *   **Bottom**: Jacks (In, Out).
*   **Layout Logic**: Knobs on top, signal flow bottom.

### Technical Specifications
*   **Delay Chip**: PT2399.
*   **Regulator**: L78L05 (Onboard +5V generation from +12V rail).
*   **Op-Amps**: TL072 for input buffering and output mixing.
*   **Delay Range**: Tuned for "Musical" range, but allows pushing into "Garbage" range (clock noise visible).

### Exclusions
*   **CV Control**: To keep it "Simple", there is NO Voltage Control over Time or Feedback. Knobs only.
*   **Tap Tempo**: Not possible with the PT2399 logic.
*   **Dual Channel**: Keeping it single channel for simplicity. Build two if you need stereo!
