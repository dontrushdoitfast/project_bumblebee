# Clock Module Code Instructions

## Setup
1.  **Install MicroPython**: Hold the BOOTSEL button on the Pico, plug it into USB. Drag the `.uf2` file (download from raspberrypi.com) onto the `RPI-RP2` drive.
2.  **IDE**: Open **Thonny IDE**. Select interpreter "MicroPython (Raspberry Pi Pico)".

## File Structure
Copy these files to the Pico:
*   `main.py`: The application logic.
*   `lib/`:
    *   `clock_core.py`: The high-speed timing engine.
    *   `europi_subset.py`: Helper classes (Knob, Button) extracted from EuroPi.
    *   `lcd_api.py` & `i2c_lcd.py`: Drivers for the 2004 Screen.

## Dependencies (LCD Drivers)
You need to download the standard LCD drivers.
1.  Go to `https://github.com/dhylands/python_lcd/tree/master/lcd`
2.  Download `lcd_api.py` and `i2c_lcd.py`.
3.  Save them into the `lib/` folder on your Pico.

## Testing
1.  **Hardware Test**: When you run `main.py`, the screen should light up.
2.  Turn the **Master Knob**: BPM should change on screen.
3.  **LED Check**: Press the buttons. Green LEDs (Channel Select) and Red LEDs (Option Select) should cycle.
4.  **Output Check**: Connect Out 1 to a scope or LED. It should blink at the BPM rate.

## Troubleshooting
*   **ImportError**: Make sure the `lib` folder exists and contains all 4 python files.
*   **Screen Dark**: Adjust the blue potentiometer on the back of the I2C backpack.
