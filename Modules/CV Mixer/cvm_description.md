# CV Mixer Description and Requirements

### Description
The **CV Mixer** is a 3-channel active mixer designed to sum both audio and CV signals. Unlike a passive mixer, it uses an Op-Amp (TL072) to ensure signals are mixed without volume loss or crosstalk. It is DC-coupled, meaning it works equally well for mixing audio sources (like oscillators) or control voltages (like LFOs and Envelopes).

### Requirements
1.  **Function**: Sum three input signals into a single output with individual level control for each channel.
2.  **Format**: Eurorack standard (3.5mm jacks).
3.  **Active Design**: Uses TL072 Op-Amp to provide Unity Gain summing (1:1 output when pot is maxed).
4.  **Interface**: 3 Input channels with dedicated attenuators.

### Panel Layout / Interface
*   **Width**: 6HP
*   **Inputs**: 3x 3.5mm Jacks (Vertical arrangement).
*   **Outputs**: 1x 3.5mm Jack (Summed Output).
*   **Controls**: 3x Potentiometers (Linear) for input attenuation.
*   **Layout Logic**:
    *   Top: Channel 1 (In + Pot)
    *   Middle: Channel 2 (In + Pot)
    *   Bottom: Channel 3 (In + Pot) + Master Output Jack.

### Technical Specifications
*   **Power Consumption**: Active module, requires +/-12V.
    *   +12V: ~10mA
    *   -12V: ~10mA
*   **Op-Amp**: TL072 (Dual Op-Amp).
    *   Stage 1: Inverting Summing Amplifier.
    *   Stage 2: Inverting Buffer (to restore correct signal phase).
*   **Impedance**: 100k Input Impedance per channel.
*   **Voltage Range**: Capable of handling standard +/-10V Eurorack signals.

### Exclusions
*   **Expansion**: No expansion headers for daisy-chaining.
*   **Mutes**: No dedicated mute switches (turn knob to 0).
