
# Bumblebee Hardware Library
# Adapted from EuroPi (Allen Synthesis)
# Licensed under Apache 2.0 (as per original source)

from machine import Pin, ADC, PWM
import time

# --- Constants ---

HIGH = 1
LOW = 0
MAX_UINT16 = 65535

# Note: Bumblebee Standards for Protection
# 100k Series Input Resistor -> 3.3V Clamp
# Means 10V Input = ~3.3V ADC Reading (Full Scale)
# But calibration handles the specifics.

class DigitalInput:
    """
    Handles reading digital inputs (Gates/Triggers) with debouncing.
    """
    def __init__(self, pin_id, debounce_ms=10):
        self.pin = Pin(pin_id, Pin.IN)  # External pull-down usually required/prudent
        self.debounce_ms = debounce_ms
        self.last_press_time = 0
        self.state = 0
        
    def value(self):
        """Returns the raw value (0 or 1)"""
        return self.pin.value()
        
    def is_pressed(self):
        """
        Returns True if high. Functional alias for value() == 1.
        """
        return self.pin.value() == 1

class Button(DigitalInput):
    """
    Extension of DigitalInput for UI Buttons (Tactile).
    Usually requires Pull-Down if not provided by hardware (Pico has internal PULL_DOWN).
    """
    def __init__(self, pin_id, debounce_ms=50):
        super().__init__(pin_id, debounce_ms)
        self.pin = Pin(pin_id, Pin.IN, Pin.PULL_DOWN) 
        # Bumblebee Standard: Buttons connect 3.3V to Pin. Ground via internal Pull-Down.

    def was_pressed(self):
        """
        Returns True if button was newly pressed since last check (Rising Edge).
        Simple state-based debouncing.
        """
        curr = self.pin.value()
        now = time.ticks_ms()
        
        if curr == 1 and self.state == 0:
            if time.ticks_diff(now, self.last_press_time) > self.debounce_ms:
                self.last_press_time = now
                self.state = 1
                return True
        elif curr == 0:
            self.state = 0
            
        return False

class Knob:
    """
    Handles Analog Inputs (Potentiometers) with smoothing.
    """
    def __init__(self, pin_id, samples=64, deadzone=0.02):
        self.adc = ADC(Pin(pin_id))
        self.samples = samples
        self.deadzone = deadzone
        
    def read_u16(self):
        """
        Return the raw u16 value (smoothed).
        """
        val = 0
        for _ in range(self.samples):
            val += self.adc.read_u16()
        return int(val // self.samples)
        
    def percent(self):
        """
        Returns 0.0 to 1.0.
        Applies deadzone at edges to ensure clean 0 and 1.
        """
        raw = self.read_u16() / MAX_UINT16
        
        # Apply Deadzone
        if raw < self.deadzone: return 0.0
        if raw > (1.0 - self.deadzone): return 1.0
        
        # Rescale the middle
        # (val - min) / (max - min)
        return (raw - self.deadzone) / (1.0 - (2 * self.deadzone))
        
    def choice(self, values):
        """
        Selects a value from a list based on knob position.
        """
        idx = int(self.percent() * len(values))
        if idx >= len(values): idx = len(values) - 1
        return values[idx]

    def range(self, steps):
        """
        Returns a value from 0 to steps.
        Useful for mapping knob to integer ranges (e.g. 0-255).
        """
        return int(self.percent() * steps)

class ScaleLogic:
    """
    Logic for Quantization.
    Kept separate from hardware, but commonly used.
    """
    # ... (To be populated if needed, or keeping it in Quantizer module is fine)
    pass
