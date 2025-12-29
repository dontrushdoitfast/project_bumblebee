# Quantizer Software Design

### Overview
This software acts as a **Dual Channel Quantizer** with a **Piano Interface**. It reads two independent analog inputs, maps them to the *same* set of allowed notes (defined by the user), and outputs precise voltages via two I2C DACs.

### Directory Structure
```
/Modules/Quantizer/Code/
├── main.py            # Entry point & Core Loop
├── lib/
│   ├── mcp4725.py     # Driver for the DACs
│   ├── neopixel.py    # Standard MicroPython NeoPixel library
│   ├── scale_logic.py # Manages active notes (C, C#, D...)
│   └── inputs.py      # Handles ADC reading & Button scanning (Wraps shared lib)
├── ../../Shared/
│   └── bumblebee_hardware.py # SHARED HARDWARE LIB (Knob, Button)
```

### 1. State Management
Instead of "Major/Minor" presets, we track the state of 12 individual notes.

**Global State:**
*   `active_notes`: List of 12 Booleans (Index 0=C, 1=C#, etc.). Default: C Major (T, F, T, F, T, T, F, T, F, T, F, T).
*   `last_note_A`: Integer (0-127) - The last MIDI note played on Channel A.
*   `last_note_B`: Integer - The last MIDI note played on Channel B.

**Persistence:**
*   **File**: `settings.json` stored in Flash.
*   **Trigger**: On every button press, update the `active_notes` in memory.
*   **Strategy**: To avoid wearing out Flash, only write to disk if no buttons have been pressed for 5 seconds (Debounce/Coalesce writes).
*   **On Boot**: Load `settings.json` if it exists, otherwise default to C Major.

### 2. The Core Loop
**Strategy**: High-speed loop reading ADCs and updating DACs. Button scanning happens every loop or via IRQ.

**Logic:**
1.  **Read Inputs**:
    *   Read `ADC0` (CV In A). Scale to Note Number (Float, e.g., 60.4).
    *   Read `ADC1` (CV In B). Scale to Note Number.
2.  **Quantize (The "Snap" Logic)**:
    *   For each channel, check the input Note Number.
    *   Look at `active_notes`.
    *   Find the **nearest enabled note**. (If C# is disabled, snap up to D or down to C).
3.  **Update Outputs**:
    *   Write value to `DAC_A (0x60)` and `DAC_B (0x61)`.
4.  **Update LEDs**:
    *   **Base Layer**: If `active_notes[i]` is True, set LED[i] to **Dim Color** (e.g., Blue). Else OFF.
    *   **Activity Layer**: If Channel A is playing C, set LED[0] to **Bright Red**. If Channel B is playing C, set LED[0] to **Bright Green**. (Mix to Yellow if both).
    *   *Optimization*: Only push NeoPixel data if state changed.

### 3. User Interface (The Piano)
**Buttons 1-12**:
*   Simple Toggle: Press Button 0 (C) -> Toggle `active_notes[0]`.
*   Feedback: LED immediately changes from Off to Dim (or vice-versa).
*   *Safety*: Prevent disabling *all* notes (forcing at least ione note to stay active).

### 4. Hardware Drivers
**Dual DACs**:
*   Initialize two instances of `MCP4725`: one at default address, one at alternate.

**NeoPixels (PL9823)**:
*   Use `machine.bitstream` or `neopixel` library.
*   Single Pin (e.g., GP0) drives all 12 LEDs.

### 5. Implementation Roadmap
1.  **DAC Test**: Communicate with MCP4725 and output calibrated voltages (1V, 2V, 3V).
2.  **Input Reading**: Read CV In and print raw values. Determine scaling factor.
3.  **Quantization Logic**: Implement the math to snap float values to scale integers.
4.  **UI Integrated**: Allow knob/button to change parameters.
