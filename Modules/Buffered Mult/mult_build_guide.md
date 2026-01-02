# Buffered Mult Build Guide

## Bill of Materials (BOM)

| Component | Value | Quantity | Notes |
| :--- | :--- | :--- | :--- |
| **Chips** | | | |
| Op-Amp | TL074 | 1 | Quad Op-Amp (We use 3 channels) |
| **Resistors** | | | |
| Input | 100k | 1 | Pull-down (to prevent floating) |
| Output Protection | 1k | 3 | One per output jack |
| **Capacitors** | | | |
| Bypass | 100nF | 2 | Power rail noise filtering |
| **Mechanical** | | | |
| Jacks | 3.5mm Mono | 4 | Panel Mount / Chassis Socket |
| Power Header | 10-pin Male | 1 | For Eurorack power connection |

## Circuit Layout
*   **Input Jack** -> Tip connected to TL074 Pins 3, 5, 10 (Non-Inverting Inputs).
*   **Feedback**:
    *   Pin 1 (Out A) -> Pin 2 (In A -)
    *   Pin 7 (Out B) -> Pin 6 (In B -)
    *   Pin 8 (Out C) -> Pin 9 (In C -)
*   **Outputs**:
    *   Pin 1 -> 1k Resistor -> Out Jack 1 Tip
    *   Pin 7 -> 1k Resistor -> Out Jack 2 Tip
    *   Pin 8 -> 1k Resistor -> Out Jack 3 Tip
