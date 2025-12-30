from machine import Pin, I2C
import time
# Assumes bumblebee_hardware.py is available
from bumblebee_hardware import Knob, Button
# from lib.i2c_lcd import I2cLcd # Commented out until user installs driver

# --- CONFIG ---
PINS = {
    'SDA': 0, 'SCL': 1,
    'ENC_A': 10, 'ENC_B': 11, 'ENC_SW': 12,
    'ENC_KNOB_ADC': 26, # Master BPM
    'BTN_CHAN': 16, 'KNOB_CHAN_ADC': 27,
    'BTN_OPT': 17, 'KNOB_OPT_ADC': 28,
    'LEDS_CHAN': [13, 14, 15], # Out 2, 3, 4
    'LEDS_OPT': [6, 7, 8],     # Swing, Euclid, Jitter
    'OUTS': [2, 3, 4, 5]       # Jack 1, 2, 3, 4
}

# --- HARDWARE SETUP ---
# leds_chan = [Pin(p, Pin.OUT) for p in PINS['LEDS_CHAN']]
# leds_opt = [Pin(p, Pin.OUT) for p in PINS['LEDS_OPT']]
btn_chan = Button(PINS['BTN_CHAN'])
btn_opt = Button(PINS['BTN_OPT'])
knob_master = Knob(PINS['ENC_KNOB_ADC'])

# --- STATE ---
selected_chan = 0 # 0=Out2, 1=Out3, 2=Out4
selected_opt = 0  # 0=Swing, 1=Euclid, 2=Jitter

def update_leds():
    # Simple logic to light up the selected LED
    # for i in range(3):
    #     leds_chan[i].value(1 if i == selected_chan else 0)
    #     leds_opt[i].value(1 if i == selected_opt else 0)
    pass


# --- CLOCK ENGINE ---
# Instantiate Core
# (Assuming PINS['OUTS'] is correct: [2, 3, 4, 5])
from lib.clock_core import ClockCore
core = ClockCore(PINS['OUTS'])

def main():
    global selected_chan, selected_opt
    
    print("Clock System Booting...")
    
    last_ui_update = 0
    
    while True:
        now = time.ticks_ms()
        
        # --- CLOCK ENGINE (High Priority) ---
        core.update() # Run the tick logic
        
        # --- UI LOOP (Every 50ms) ---
        if time.ticks_diff(now, last_ui_update) > 50:
            last_ui_update = now
            
            # Check Buttons
            if btn_chan.was_pressed():
                selected_chan = (selected_chan + 1) % 3
                print(f"Channel Selected: {selected_chan}")
                update_leds()
                
            if btn_opt.was_pressed():
                # TODO: Check for LONG PRESS (Reset) here
                selected_opt = (selected_opt + 1) % 3
                print(f"Option Selected: {selected_opt}")
                update_leds()
                
            # Check Knobs
            bpm = 30 + knob_master.range(270) # 30 to 300 BPM
            core.set_bpm(bpm)
            # print(f"BPM: {bpm}")


if __name__ == '__main__':
    main()
