# Quantizer Description and Requirements

**Difficulty: ⭐⭐⭐⭐ Advanced** — *Pico + I2C DACs + LED strip + 12 buttons. Requires calibration.*

### Description
The **Quantizer** module is a performance-oriented Dual Channel Pitch Quantizer. It uses a "Piano Keyboard" interface, allowing you to intuitively visualize and edit the selected scale. It features **2 channels** of quantization (processing two separate CV inputs) that share the same musical scale, perfect for keeping two oscillators in harmony.

### Requirements
1.  **Core Function**: Dual Channel CV Quantization.
    *   **Shared Scale**: Both channels are quantized to the same set of selected notes.
    *   **Inputs**: 2x 0-10V Control Voltages (CV A, CV B).
    *   **Outputs**: 2x Precision 0-5V Pitch Outputs (Out A, Out B).
2.  **User Interface (The Piano)**:
    *   **12x Buttons**: Arranged like a piano keyboard (C, C#, D...). Pressing a button toggles that note ON/OFF in the scale.
    *   **12x RGB LEDs**:
        *   **DIM**: Note is active in the scale.
        *   **OFF**: Note is removed from the scale.
        *   **FLASH**: Note is currently being played.
3.  **Performance**:
    *   Real-time toggling of notes.
    *   High-precision voltage generation using **2x MCP4725** DACs.

### Panel Layout / Interface
*   **The "Keyboard" (Top/Middle)**:
    *   12x Tactile Buttons arranged in a piano layout (Black keys offset).
    *   12x PL9823 Smart LEDs (one above each button).
*   **Jacks (Bottom)**:
    *   **CV In A** | **CV In B**
    *   **CV Out A** | **CV Out B**

### Technical Specifications
*   **Core**: Raspberry Pi Pico (RP2040).
*   **DAC**: **2x MCP4725** (Addresses `0x60` and `0x61`).
*   **Input Scaling**: **TL072** based buffer/scaler (10V -> 3.3V).
*   **LED Driver**: Single GPIO driving a daisy chain of **PL9823** or **WS2812** LEDs.

### Design considerations
*   **Accuracy**: The move to MCP4725 is specifically to avoid the ripple and filtering latency of PWM.
*   **Latency**: Must be low enough to feel responsive (~1ms or less).
