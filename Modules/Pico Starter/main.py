from machine import Pin, ADC, PWM
import time
import random

# --- Bumblebee Hardware Lib Copy ---
# (Ideally we import this, but for a starter standalone file we keep it self-contained or import if path allows)
# For this project structure, we will assume the User copies `bumblebee_hardware.py` to the Pico lib/ folder
# or we just write raw logic for maximum transparency/learning.
# Let's use raw logic for the "Starter" aspect to show exactly what's happening.

# --- Hardware Config ---
PIN_OUT_A = 0
PIN_OUT_B = 1
PIN_TRIG_IN = 15
PIN_BTN_MANUAL = 14
PIN_PROB_KNOB = 26

# --- Setup ---
out_a = Pin(PIN_OUT_A, Pin.OUT)
out_b = Pin(PIN_OUT_B, Pin.OUT)
led_onboard = Pin(25, Pin.OUT)

# Input Gate
# Note: Input is protected by hardware, but logic checks for High/Low
trig_in = Pin(PIN_TRIG_IN, Pin.IN, Pin.PULL_DOWN) 

# Manual Button
btn_manual = Pin(PIN_BTN_MANUAL, Pin.IN, Pin.PULL_DOWN)

# Probability Knob
adc_prob = ADC(Pin(PIN_PROB_KNOB))

# --- State ---
last_trig_state = 0
last_btn_state = 0

def get_probability():
    """Reads knob and returns 0.0 to 1.0"""
    # Read u16 (0-65535) and convert
    return adc_prob.read_u16() / 65535.0

def trigger_out(channel):
    """
    Fires a 10ms trigger on the selected channel
    channel: 'A' or 'B'
    """
    led_onboard.value(1)
    if channel == 'A':
        out_a.value(1)
        time.sleep_ms(10) # Simple blocking wait for starter simplicity
        out_a.value(0)
    else:
        out_b.value(1)
        time.sleep_ms(10)
        out_b.value(0)
    led_onboard.value(0)

print("Pico Starter: Bernoulli Gate Ready.")

while True:
    # 1. Read Inputs
    curr_trig = trig_in.value()
    curr_btn = btn_manual.value()
    
    triggered = False
    
    # Check for RISING edge on Jack Input
    if curr_trig == 1 and last_trig_state == 0:
        triggered = True
        
    # Check for RISING edge on Manual Button
    if curr_btn == 1 and last_btn_state == 0:
        triggered = True
        
    last_trig_state = curr_trig
    last_btn_state = curr_btn
    
    # 2. Logic
    if triggered:
        prob = get_probability() # 0.0 to 1.0
        rand_val = random.random() # 0.0 to 1.0
        
        # Decide output
        # If prob is 1.0 (100%), we want OUT A always.
        # If prob is 0.0 (0%), we want OUT B always.
        # If prob is 0.5, we want 50/50.
        
        if rand_val < prob:
            # Hit! Output A
            trigger_out('A')
        else:
            # Miss! Output B
            trigger_out('B')
            
    # Small sleep to save CPU, though for tight timing we might minimize this
    time.sleep_ms(1)
