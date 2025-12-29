# Passive Attenuator Description and Requirements 

### Description
### Description
The **Passive Attenuator** is a dual-channel utility module used to reduce the amplitude of a signal. It is essential for taming hot CV signals or lowering audio levels. 
**Usage**: 
*   **Fully Clockwise (Right)**: Unity Gain (100% signal passes through).
*   **Fully Counter-Clockwise (Left)**: Silence (0% signal passes through).
*   **In Between**: Linear scaling of the voltage.

### Requirements
1.  **Function**: Linearly attenuate an input signal from 100% (Unity) to 0% (Silent).
2.  **Format**: Eurorack standard (3.5mm jacks, 128.5mm height).
3.  **Capacity**: Two fully independent channels.
4.  **Interface**: Large, accessible knobs for precise control.

### Panel Layout / Interface
*   **Width**: 4HP
*   **Inputs**: 2x 3.5mm Jacks (Top, Lower Middle)
*   **Outputs**: 2x 3.5mm Jacks (Upper Middle, Bottom)
*   **Controls**: 2x Potentiometers (Linear)
*   **Layout Logic**:
    *   Top Half: Channel A (In -> Pot -> Out)
    *   Bottom Half: Channel B (In -> Pot -> Out)

### Technical Specifications
*   **Power Consumption**: 0mA (Passive) - No power header required.
*   **Potentiometer Used**: B50k or B100k Linear (9mm Alpha vertical or similar).
*   **Voltage Range**: +/- 12V safe (or whatever the jacks can handle).
*   **Channels**: 2 Independent Channels.
### Exclusions
Things this module will not do.