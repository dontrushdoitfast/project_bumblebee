# The Bridge Build Guide

## Bill of Materials (BOM)

| Component | Value | Quantity | Notes |
| :--- | :--- | :--- | :--- |
| **Chips** | | | |
| Microcontroller | Raspberry Pi Pico | 1 | |
| DAC | MCP4822 | 1 | 12-bit, SPI |
| Op-Amp | TL072 | 1 | Standard dual Op-Amp (Powered by +/-12V) |
| **Resistors** | | | |
| Gate Protection | 1k | 4 | For Gate Outputs |
| Gain Resistors | 10k / 39k | TBD | Non-Inverting Amp (Gain ~4.9x) to boost 2.048V to 10V |
| **Mechanical** | | | |
| Jacks | Thonkiconn | 6 | 2 CV, 4 Gate |
| USB Extension | Panel Mount | 1 | USB-C to Micro-USB (for Pico) internal cable |

## Wiring Guide
*   **SPI Connection**:
    *   Pico GPIO 19 (TX) -> MCP4822 SDI
    *   Pico GPIO 18 (SCK) -> MCP4822 SCK
    *   Pico GPIO 17 (CS) -> MCP4822 CS
*   **Gates**:
    *   Gate 1: GPIO 10
    *   Gate 2: GPIO 11
    *   Gate 3: GPIO 12
    *   Gate 4: GPIO 13
