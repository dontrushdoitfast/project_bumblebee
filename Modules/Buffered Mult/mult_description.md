# Buffered Mult Description

**Difficulty: ⭐ Very Easy** — *Simplest Op-Amp project.*

### Description
The **Buffered Mult** is a precision cloning tool. It takes 1 Input signal and creates 3 identical, electrically isolated copies.
Because it is **Buffered** (using an Op-Amp), drawing current from "Copy 1" does not cause the voltage to sag on "Copy 2". This is critical for pitch CV (V/Oct).

### Requirements
1.  **Function**: 1 Input -> 3 Outputs.
2.  **Unity Gain**: 1.000x gain (Exact copy).
3.  **High Input Impedance**: >1MΩ (Doesn't load down the source).
4.  **Low Output Impedance**: <100Ω (Can drive long cables).

### Panel Layout
*   **Width**: 2HP
*   **Jacks**:
    *   In (Top)
    *   Out 1
    *   Out 2
    *   Out 3 (Bottom)

### Technical Specifications
*   **Op-Amp**: TL074 (Quad Op-Amp) or TL072 (Dual).
    *   We need 3 buffers. A TL074 has 4 Op-Amps, so it's perfect (1 unused).
*   **Circuit**: Voltage Follower (Non-Inverting buffer).
    *   Connect Output to Inverting Input (-).
    *   Signal goes to Non-Inverting Input (+).
