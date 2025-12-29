
# Hardware Test Script ("Smoke Test Helper")
# Run this to verify pins before flashing main firmware.

from machine import Pin, Timer
import utime
from bumblebee_hardware import Knob, Button

print("--- Bumblebee Hardware Test ---")

# --- USER CONFIG: EDIT THESE PINS FOR YOUR MODULE ---
LEDS = [2, 3, 4] # Example GPIOs
BUTTONS = [14, 15] 
POTS = [26, 27]
# ----------------------------------------------------

# Setup
led_pins = [Pin(p, Pin.OUT) for p in LEDS]
btns = [Button(p) for p in BUTTONS]
knobs = [Knob(p) for p in POTS]

print(f"Testing {len(LEDS)} LEDs, {len(BUTTONS)} Buttons, {len(POTS)} Pots.")

def test_cycle():
    print("Cycling LEDs...")
    for i, led in enumerate(led_pins):
        print(f"  LED {LEDS[i]} ON")
        led.value(1)
        utime.sleep(0.2)
        led.value(0)
    print("Done.")

# Run once
test_cycle()

print("Entering Input Hardware Loop (Ctrl+C to stop)")
print("Press buttons or turn knobs to see values.")

while True:
    # Check Buttons
    for i, btn in enumerate(btns):
        if btn.was_pressed():
            print(f"BUTTON {BUTTONS[i]} PRESSED!")
            # Toggle corresponding LED if exists
            if i < len(led_pins):
                led_pins[i].toggle()

    # Check Pots (every 500ms)
    # in a real test we'd print only on change, but simple polling is fine
    # ...
    utime.sleep(0.01)
