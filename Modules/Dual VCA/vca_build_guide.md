# Dual Linear VCA Build Guide

## Bill of Materials (BOM)

| Component | Value | Quantity | Notes |
| :--- | :--- | :--- | :--- |
| **Chips** | | | |
| OTA | LM13700 | 1 | The VCA core |
| Op-Amp | TL072 | 1 | Output Buffer (Optional but recommended) |
| **Resistors** | | | |
| Input Resistors | 100k | 4 | Signal/CV Inputs |
| I_abc Resistors | 22k | 2 | Current control for OTA (Tune for 5V CV) |
| **Capacitors** | | | |
| Bypass | 100nF | 2 | Near power pins |
| **Mechanical** | | | |
| Jacks | Thonkiconn | 6 | 2 In, 2 Out, 2 CV |
| Pots | B100k | 4 | 2 Attenuators, 2 Offset |

## Circuit Notes
*   **LM13700 Logic**: The LM13700 is a "Current Controlled" amplifier. We use resistors to convert our Voltage Inputs into Current.
*   **Linearizing Diodes**: The LM13700 has specific pins for linearizing diodes. ensure these are biased correctly (~1mA) to allow for clean signal processing if Audio is used.
*   **Offset**: The "Initial Gain" knob simply injects a small amount of current into the I_abc pin, allowing the VCA to be "Open" even without CV.
