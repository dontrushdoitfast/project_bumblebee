
import machine
import utime
import neopixel
from lib.mcp4725 import MCP4725
from lib.scale_logic import ScaleLogic
from lib.inputs import Inputs

# --- CONFIGURATION ---
PIN_SDA = 8
PIN_SCL = 9
PIN_LEDS = 22
PIN_ADC_A = 26
PIN_ADC_B = 27

# Button Pins (Piano Inputs C..B)
# Update these based on your actual wiring!
# Assuming GP10..GP21 for now
BTN_PINS = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21] 

# --- SETUP ---
i2c = machine.I2C(0, sda=machine.Pin(PIN_SDA), scl=machine.Pin(PIN_SCL), freq=400000)

# Init DACs
dac_a = MCP4725(i2c, address=0x60)
dac_b = MCP4725(i2c, address=0x61) # Second DAC with A0 bridged

# Init LEDs
num_leds = 12
led_strip = neopixel.NeoPixel(machine.Pin(PIN_LEDS), num_leds)

# Init Logic
logic = ScaleLogic()
inputs = Inputs(BTN_PINS, PIN_ADC_A, PIN_ADC_B)

# Colors
COLOR_OFF = (0, 0, 0)
COLOR_ACTIVE = (0, 0, 10) # Dim Blue
COLOR_PLAY_A = (50, 0, 0) # Red
COLOR_PLAY_B = (0, 50, 0) # Green
COLOR_PLAY_BOTH = (50, 50, 0) # Yellow

last_save_check = utime.ticks_ms()
SAVE_DELAY_MS = 5000
last_action_time = 0

last_note_a = -1
last_note_b = -1

# Calibration: DAC Output
# How many DAC units (0-4095) per Semitone?
# 5V Range (approx). 1V/Octave.
# Target: 1V change per 12 notes.
# DAC units per Volt = ~4095 / 3.3 (if powered by 3.3).
# Let's say roughly 68.25 units per semitone.
DAC_UNITS_PER_SEMITONE = 68.25 
# Note 24 (0V) -> DAC 0.
# Note 36 (1V) -> DAC 819.

print("Quantizer Ready.")

while True:
    # 1. Input Scanning
    # -----------------
    # Check Buttons
    pressed_idx = inputs.scan_buttons()
    if pressed_idx != -1:
        logic.toggle_note(pressed_idx)
        last_action_time = utime.ticks_ms()
        # Force immediate LED update for UI responsiveness
        
    # Check Auto-Save
    now = utime.ticks_ms()
    if logic.dirty and (utime.ticks_diff(now, last_action_time) > SAVE_DELAY_MS):
        logic.save()
        
    # Read CVs
    raw_note_a = inputs.read_cv('A')
    raw_note_b = inputs.read_cv('B')
    
    # 2. Logic (Quantize)
    # -------------------
    q_note_a = logic.get_closest_note(raw_note_a)
    q_note_b = logic.get_closest_note(raw_note_b)
    
    # 3. Output Updates (DAC)
    # -----------------------
    if q_note_a != last_note_a:
        # Map MIDI Note to DAC Value
        # Formula: (Note - 24) * Scale. Clip to 0-4095.
        val = int((q_note_a - 24) * DAC_UNITS_PER_SEMITONE)
        dac_a.write(val)
        last_note_a = q_note_a
        
    if q_note_b != last_note_b:
        val = int((q_note_b - 24) * DAC_UNITS_PER_SEMITONE)
        dac_b.write(val)
        last_note_b = q_note_b

    # 4. LED Visualization
    # --------------------
    # Calculate which notes correlate to "Piano Keys" (0-11)
    # q_note_a is like 60 (C4). 60 % 12 = 0 (C).
    key_a = q_note_a % 12
    key_b = q_note_b % 12
    
    changes = False
    for i in range(12):
        # Determine Color
        color = COLOR_OFF
        
        if logic.active_notes[i]:
            color = COLOR_ACTIVE
            
        # Overlay Play States
        is_a = (key_a == i)
        is_b = (key_b == i)
        
        if is_a and is_b:
            color = COLOR_PLAY_BOTH
        elif is_a:
            color = COLOR_PLAY_A
        elif is_b:
            color = COLOR_PLAY_B
            
        # Update Strip buffer
        # (Assuming we matched the wiring zig-zag in software or physically kept it 0-11)
        if led_strip[i] != color:
             led_strip[i] = color
             changes = True
             
    if changes:
        led_strip.write()
        
    # Small sleep to yield? No, run fast for quantization!
    # But maybe 1ms to keep USB serial happy?
    # utime.sleep_us(100)
