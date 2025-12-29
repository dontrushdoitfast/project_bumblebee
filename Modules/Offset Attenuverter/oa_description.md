# Offset / Attenuverter Description and Requirements

### Description
The **Offset / Attenuverter** is a critical utility module for controlling Control Voltage (CV) signals. It performs two main functions:
1.  **Attenuversion**: Attenuates (reduces) and Inverts the incoming signal. A knob at 12 o'clock is 0V (silence). Clockwise adds the signal (up to 1x gain). Counter-clockwise subtracts/inverts the signal (up to -1x gain).
2.  **Offset**: Adds a fixed DC voltage to the signal (e.g., shifting a -5V to +5V LFO to be 0V to +10V).

This functionality is essential for making modulation sources compatible with different module inputs (e.g., tuning an envelope to perfectly open a filter).

### Requirements
1.  **Input**: Bipolar CV or Audio (typically +/- 5V or +/- 10V).
2.  **Output**: The processed signal (Input * Gain) + Offset.
3.  **Controls**:
    *   **Attenuverter Knob**: Bipolar potentiometer (-1 to +1 gain).
    *   **Offset Knob**: Bipolar potentiometer (typically +/- 5V or +/- 10V shift).
4.  **Indicators**:
    *   Bipolar LED (Green = Positive, Red = Negative) to visualize the output.
5.  **Interface**:
    *   Input Jack.
    *   Output Jack.

### Panel Layout / Interface
*   **Width**: 4HP
*   **Controls**:
    *   **Top**: Input Jack.
    *   **Upper Mid**: Attenuverter Potentiometer (Center Detent preferred).
    *   **Lower Mid**: Offset Potentiometer.
    *   **Bottom**: Output Jack and Bipolar LED.
*   **Layout Logic**: Signal flows down. Input -> Process -> Output.

### Technical Specifications
*   **Topology**: Op-Amp based analog computer.
*   **Active Components**: TL072 or TL074 Op-Amps.
    *   Stage 1: Input Buffer / Inverter.
    *   Stage 2: Summing Amplifier (Signal + Offset).
*   **Impedance**: High input impedance (100k) to prevent loading source modules.
*   **Protection**: 1k resistor on output to protect op-amp from accidental shorts.

### Exclusions
*   **Precision**: This is a performance module, not a precision 1V/Oct transposition tool (though it can work for that, precise resistors are not strictly required).

### Usage Tips (with Quantizers)
This module acts differently depending on how you use it with a Pitch Quantizer:
*   **Offset -> Quantizer**: **Safe**. You can use the Offset knob to transpose melodies. Precision is not critical because the quantizer will "snap" the imprecise voltage to the nearest perfect semitone. Tune by ear until the key changes.
*   **Attenuverter -> Quantizer**: **Use with Caution**. Attenuating a pitch sequence (e.g., 0.5x gain) shrinks the intervals (Octaves become Tritones). Do not use the Attenuverter on pitch CV if you want to maintain standard 1V/Octave scaling, unless you are intentionally creating microtonal or experimental scales.
