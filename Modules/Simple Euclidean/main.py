from machine import Pin, ADC
import time

# --- PINS ---
PIN_OUT_A = 0
PIN_OUT_B = 1
PIN_TRIG_IN = 15
PIN_BTN_RESET = 14
PIN_KNOB = 26

# --- HARDWARE ---
out_a = Pin(PIN_OUT_A, Pin.OUT)
out_b = Pin(PIN_OUT_B, Pin.OUT)
led = Pin(25, Pin.OUT)

trig_in = Pin(PIN_TRIG_IN, Pin.IN, Pin.PULL_DOWN)
btn_reset = Pin(PIN_BTN_RESET, Pin.IN, Pin.PULL_DOWN)
adc_knob = ADC(Pin(PIN_KNOB))

# --- STATE ---
step = 0
TOTAL_STEPS = 16
last_trig_state = 0
last_btn_state = 0

def get_hits():
    # Map 0-65535 to 0-16
    val = adc_knob.read_u16()
    # Simple division
    return int((val / 65535.0) * 16.9) # 16.9 ensures we can reach 16

def is_beat(curr_step, hits, total):
    if hits == 0: return False
    if hits >= total: return True
    
    # Bresenham-like Logic for Euclidean Rhythms
    # (step * hits) % total < hits  <-- This is one way, but simple accumulation is easier
    
    # Standard "Bjorklund" distribution check:
    # A beat exists at this step if:
    # floor(step * hits / total) != floor((step-1) * hits / total)
    # But for a looping sequencer, we just check the current bucket.
    
    # Let's use the simple accumulator usage:
    # bucket += hits. if bucket >= total, fire and subtract total.
    # That works for generation, but we need random access based on 'step'.
    
    # The Formula: (step * hits) // total  <- Does this value change?
    previous_val = ((curr_step - 1) * hits) // total
    current_val = (curr_step * hits) // total
    return current_val != previous_val

def fire(channel):
    p = out_a if channel == 'A' else out_b
    p.value(1)
    led.value(1)
    # 10ms pulse
    time.sleep_ms(10) 
    p.value(0)
    led.value(0)

# --- LOOP ---
print("Euclidean Generator Ready.")

while True:
    # Read Hardware
    curr_trig = trig_in.value()
    curr_btn = btn_reset.value()
    
    # Clock Input (Rising Edge)
    if curr_trig == 1 and last_trig_state == 0:
        step = (step + 1) % TOTAL_STEPS
        
        hits = get_hits()
        
        # Calculate Euclidean Beat
        # Using the standard: 1 if (step * hits) % total < hits
        # Note: This aligns hits to start at 0.
        is_hit = ((step * hits) % TOTAL_STEPS) < hits
        
        if is_hit:
            fire('A')
        else:
            fire('B')
            
    # Reset Button (Rising Edge)
    if curr_btn == 1 and last_btn_state == 0:
        step = 0
        print("Reset!")
        # Optional: Flash LED to confirm
        
    last_trig_state = curr_trig
    last_btn_state = curr_btn
    
    time.sleep_ms(1)
