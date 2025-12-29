
from machine import Pin, ADC
import utime

class Inputs:
    def __init__(self, btn_pins, cv_pin_a, cv_pin_b, calibration=None):
        # Buttons: List of GPIO numbers
        self.buttons = [Pin(p, Pin.IN, Pin.PULL_UP) for p in btn_pins]
        self.last_btn_states = [1] * 12
        self.last_btn_time = 0
        
        # ADC
        self.adc_a = ADC(cv_pin_a)
        self.adc_b = ADC(cv_pin_b)
        
        # Calibration object (or use defaults)
        self.calibration = calibration
        
    def scan_buttons(self):
        """
        Returns index of pressed button or -1.
        Simple logic: Returns first pressed button found.
        """
        now = utime.ticks_ms()
        if utime.ticks_diff(now, self.last_btn_time) < 200: # Debounce default
            return -1
            
        for i, btn in enumerate(self.buttons):
            val = btn.value()
            if val == 0 and self.last_btn_states[i] == 1: # Falling Edge (Pressed)
                self.last_btn_states[i] = 0
                self.last_btn_time = now
                return i
            elif val == 1:
                self.last_btn_states[i] = 1
        return -1

    def read_cv(self, channel='A'):
        """
        Returns input as a float Note Number (e.g. 60.0 = C4).
        Uses calibration object if available.
        """
        # Oversample for noise reduction (EuroPi uses 32)
        raw = 0
        adc = self.adc_a if channel == 'A' else self.adc_b
        for _ in range(32):
            raw += adc.read_u16()
        raw //= 32
        
        # Use calibration object if available
        if self.calibration:
            return self.calibration.adc_to_note(raw)
        
        # Fallback to defaults (shouldn't happen if properly initialized)
        # Default: 12000 raw units per volt, 0V = Note 24
        volts = raw / 12000.0
        return 24 + (volts * 12)

