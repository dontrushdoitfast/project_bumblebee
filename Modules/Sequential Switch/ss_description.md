# Sequential Switch Description and Requirements

### Description
The **Sequential Switch** is a 4-step bidirectional router. It can be used in two modes:
1.  **Demultiplexer (1-to-4)**: Send one source (e.g., LFO) to 4 different destinations sequentially.
2.  **Multiplexer (4-to-1)**: Select between 4 different sources (e.g., 4 waveforms) and send them to one output.

The design is based on the **CD4017** Decade Counter (which does the counting) and the **CD4051** Analog Multiplexer (which does the switching). By running the CD4051 on +/- rails (-12V on VEE), it can handle **bipolar Audio and CV signals** cleanly without clipping.

### Requirements
1.  **Steps**: 4 Steps fixed.
2.  **Direction**: Forward only (Classic 4017 behavior).
3.  **Signal Path**: Bidirectional and AC/DC connected.
4.  **Interface**: 
    *   **Inputs**: Clock, Reset.
    *   **I/O**: Common I/O Jack, 4x Channel I/O Jacks.
    *   **Feedback**: LED per step to show active channel.
5.  **Power**: StandardEurorack +/-12V.

### Panel Layout / Interface
*   **Width**: 4HP
*   **Controls**:
    *   **Top**: Clock Input, Reset Input.
    *   **Middle**: Common I/O Jack.
    *   **Bottom**: 4x Channel Jacks, each with an LED next to it.
*   **Layout Logic**: Top-down flow (Control -> Active IO -> Channel IO).

### Technical Specifications
*   **Logic Core**: CD4017 (Counter) driving address pins of CD4051.
*   **Switching Element**: Texas Instruments CD4051BE (or similar).
*   **Voltage Range**: +/- 10V (Headroom limited by +/-12V supply).
*   **Clock Input**: Expects standard +5V gate/trigger.

### Exclusions
*   **Step Addressing**: You cannot jump to arbitrary steps (e.g., via extra CV input); it only steps 1-2-3-4.
*   **Reverse**: It does not step backwards (requires Up/Down counter chips).
