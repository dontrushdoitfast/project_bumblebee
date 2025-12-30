# Dual Linear VCA Description and Requirements

**Difficulty: ⭐⭐ Easy** — *Standard Op-Amp / OTA circuit.*
    
### Description
The **Dual Linear VCA** is a "Utility" Voltage Controlled Amplifier. While the 2600 has VCAs for audio, this module is optimized for **Modulation**. It allows you to use one CV (e.g., an Envelope or Mod Wheel) to control the amplitude of another CV (e.g., LFO depth).
It uses a **Linear** response curve, which is mathematically accurate for controlling CV depth (unlike Logarithmic VCAs which are better for audio volume).

### Requirements
1.  **Function**: 2 Independent VCA channels.
2.  **Response**: Linear (Best for CV).
3.  **Control**:
    *   **CV Input**: 0V = Silent, 5V = Unity Gain.
    *   **Gain Knob**: Sets the initial level or biases the CV.
    *   **Attenuator**: Controls how much the CV input affects the VCA.

### Panel Layout
*   **Width**: 6HP
*   **Channel 1 (Top)**:
    *   Signal In
    *   Signal Out
    *   CV In
    *   CV Attenuator Knob
    *   Initial Gain/Offset Knob
*   **Channel 2 (Bottom)**: Same as Channel 1.

### Technical Specifications
*   **Core Chip**: LM13700 (Dual OTA).
*   **Voltage**: +/-12V.
*   **Input**: DC Coupled (Accepts Audio or CV).
