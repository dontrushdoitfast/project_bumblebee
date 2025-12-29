
from machine import Pin, ADC
import utime

class Inputs:
    def __init__(self, btn_pins, cv_pi_a, cv_pin_b):
        # Buttons: List of GPIO numbers
        self.buttons = [Pin(p, Pin.IN, Pin.PULL_UP) for p in btn_pins]
        self.last_btn_states = [1] * 12
        self.last_btn_time = 0
        
        # ADC
        self.adc_a = ADC(cv_pi_a)
        self.adc_b = ADC(cv_pin_b)
        
        # Calibration (To be tuned by user)
        # ADC(u16) -> Volts -> Octaves
        # 3.3V Input = 65535 Raw.
        # But we used a 10V->3.3V divider (approx 1/3).
        # So 1V Input = ? Raw. 
        # Default assumption: 1V/Octave.
        # Let's say 12000 Raw = 1V (Octave).
        self.calibration_scale = 12000.0 # Raw units per 1.00V (1 Octave / 12 Semitones)
        
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
        """
        # Oversample for noise reduction (EuroPi uses 32)
        raw = 0
        adc = self.adc_a if channel == 'A' else self.adc_b
        for _ in range(32):
            raw += adc.read_u16()
        raw //= 32
        
        # Math: Raw / Scale = Octaves. Octaves * 12 = Semitones.
        # We start at MIDI note 0? Or 24 (C1)? Let's assume 0V = Note 24 (C1).
        
        octaves = raw / self.calibration_scale
        note_num = 24 + (octaves * 12)
        return note_num
