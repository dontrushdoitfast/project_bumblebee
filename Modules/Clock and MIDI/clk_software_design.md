# Clock Generator Software Design

### Overview
This document outlines the MicroPython architecture for the **Smart Lab Clock**. The software needs to handle high-speed timing (Clocks) concurrently with a slow user interface (Screen/Buttons), without allowing the UI to interrupt the rhythm.

### Directory Structure
```
/Modules/Clock and MIDI/Code/
├── main.py            # Entry point & Core Loop
├── lib/
│   ├── lcd_api.py     # Library for 2004 LCD
│   ├── i2c_lcd.py     # I2C driver for LCD
│   ├── europi.py      # COPY OF EUROPI LIBRARY (Subset)
│   │   ├── Class Knob # Essential for smoothing ADC
│   │   └── Class Button # Essential for debouncing
│   ├── clock_core.py  # The timing engine (Class)
│   └── ui.py          # Handling Buttons, Pots, and LEDs
```

### 1. State Management (The Data Model)
We need a central dictionary or class to store the state of the system so the UI and Engine can access it.

**Global State:**
*   `master_bpm`: Integer (e.g., 120)
*   `is_running`: Boolean
*   `swing_amount`: 0-100%
*   `jitter_amount`: 0-100%
*   `euclid_steps`: Integer (1-16) for Out 4
*   `euclid_hits`: Integer (1-16) for Out 4

**Channel Configs (Array of 3):**
*   `channels[0]` (Out 2): Division Ratio (e.g., 4 = Quarter Note)
*   `channels[1]` (Out 3): ...
*   `channels[2]` (Out 4): ...

**UI State:**
*   `selected_channel_index`: 0, 1, or 2 (Out 2/3/4)
*   `selected_option_index`: 0=Swing, 1=Euclid, 2=Jitter

### 2. The Core Clock Loop
**Strategy**: Use `utime.ticks_us()` in a non-blocking `while True` loop (Super Loop) or a Timer Interrupt.
*   *Preference*: **Timer Interrupt** for the master clock ticks to ensure stability, while the main loop handles UI.

**Logic:**
1.  **PPQN (Pulses Per Quarter Note)**: Internal resolution should be high (e.g., 96 PPQN) to handle Swing and Jitter smoothly.
2.  **Swing Logic**:
    *   On even 16th notes, delay the trigger by `swing_amount` milliseconds.
3.  **Euclidean Logic (Out 4)**:
    *   Use the standard algorithm: `(step_count * hits) // total_steps`.
    *   If the result changes integer value, fire a pulse.

### 3. User Interface (The "Modal" Workflow)
**Button Handling**:
*   **Reuse EuroPi `Button` Class**: It handles debouncing (`debounce_delay`) and rising/falling edge interrupts perfectly.
*   **Long Press (Reset)**:
    *   Monitor duration of "Option Button" press.
    *   If `duration > 3000ms`: Trigger `reset_options()` function.
    *   *Feedback*: Flash all Options LEDs to confirm reset.
*   **Action**: Increment `selected_channel_index` or `selected_option_index` (on Short Press). Update LEDs immediately.

**Potentiometer Handling ("Soft Takeover")**:
*   **Reuse EuroPi `Knob` Class**: Use `.percent()` or `.range(steps)` to get clean values without jitter.
*   *Problem*: If Output 2 is set to "Div 4", and you switch to Output 3 which is "Div 16", but the knob is physically at "Div 4", turning it might jump Out 3 suddenly.
*   *Solution*: **Latch Mode**. The value doesn't update until the physical knob passes through the stored value.
    *   Implementation: Store `last_knob_val`. Compare `current_knob_val`. Only update `state` if they cross.

**Display**:
*   Update screen only when values change (Flag-based updates) to save CPU cycles.
*   Line 1: BPM / Status
*   Line 2: Out 2 Setting | Out 3 Setting
*   Line 3: Out 4 Setting (Euclid info)
*   Line 4: Swing % | Jitter %

### 4. Input Protection (Software Side)
*   **Clock In**: The external clock input pin needs a `Pin.irq(trigger=Pin.IRQ_RISING, handler=sync_callback)`.
*   **Sync**: When external pulse received, reset internal PPQN counter to aligns the downbeat.

### 5. Implementation Roadmap
1.  **Hardware Test**: Verify LCD, Buttons, Pots, and LEDs work individually.
2.  **Clock Engine**: Get a stable pulse out of Pin 2 at 120 BPM.
3.  **UI Integration**: Connect the Knobs to the Variables.
4.  **Advanced Features**: Add Swing math and Euclidean algorithm.
