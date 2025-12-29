# Power Supply Description and Requirements

**Difficulty: ⭐⭐ Easy** — *Introduces rectification and voltage regulators. Requires careful polarity checks.*

### Description
The **Power Supply** is the heart of the system. It takes AC power from an external "wall wart" transformer and converts it into the stable **+12V and -12V DC** rails required by Eurorack modules. 
The design uses a **Linear** topology with L7812 (Positive) and L7912 (Negative) voltage regulators. While less efficient than switching supplies, linear supplies are preferred for analog audio because they generate very little noise/ripple.

### Requirements
1.  **Input**: 12V to 15V **AC** (Alternating Current). *Note: DC wall warts will NOT work for the negative rail.*
2.  **Output**: Regulated +12V and -12V DC.
3.  **Current Capacity**: Approx 500mA - 1A per rail (limited by the wall wart and heatsinking).
4.  **Protection**: Fuses (PTC) and Diodes to prevent damage from faults.
5.  **Interface**: 
    *   **Front Panel**: Power Switch, LED Indicators (+12V/-12V), and Barrel Jack Input.
    *   **Rear**: Standard 10-pin Eurorack bus board connection.

### Panel Layout / Interface
*   **Width**: 4HP (Dedicated Module)
    *   *Design Choice*: A dedicated module provides a safe, panel-mounted entry point for AC power and visual confirmation of rail status (LEDs). This is superior to hidden bus board supplies for safety and debugging.
*   **Controls**:
    *   **Top**: 2.1mm DC Barrel Jack (Center Pin technically irrelevant for AC, but standard fit).
    *   **Middle**: SPST Toggle Switch (Power On/Off).
    *   **Bottom**: Two LEDs (Green = +12V OK, Red = -12V OK).
*   **Layout Logic**: Power enters top, filtered and switched, status shown at bottom.

### Technical Specifications
*   **Topology**: Linear Half-Wave Rectifier + Series Regulators.
*   **Regulators**: L7812 (+12V) and L7912 (-12V).
*   **Filter Capacitors**: 2200uF or larger recommended to reduce ripple.
*   **Heat Dissipation**: Regulators will get warm/hot under load; consider heatsinks if drawing >200mA.

### Exclusions
*   **5V Rail**: This design does NOT include a 5V regulator (Pico modules usually generate their own 5V/3.3V from 12V).
*   **High Power**: Not intended to power massive cases; designed for this specific skiff (approx 84HP).
