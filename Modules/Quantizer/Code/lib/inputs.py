from machine import Pin, ADC
import utime
# Assumes bumblebee_hardware.py is available in path (e.g. inside lib/)
from bumblebee_hardware import Button, Knob

class Inputs:
    def __init__(self, btn_pins, cv_pin_a, cv_pin_b, calibration=None):
        # Buttons: List of Button objects (Standard: Pull-Down via Bumblebee Lib)
        # Note: Hardware has external Pull-Ups? 
        # WAIT: The build guide says "Buttons: GP10-GP21 (Internal PULL_DOWN)" in my new text.
        # But old code had "Pin.PULL_UP"?
        # Let's check the old code line I am replacing: "Pin(p, Pin.IN, Pin.PULL_UP)"
        # The OLD code used Pull-Up. My new build guide (and EuroPi standard) implies Pull-Down for active-high buttons.
        # I MUST stick to the NEW standard (Bumblebee "Prudent" = EuroPi-like).
        # So I will use the Button class which defaults to Pull-Down safe logic.
        self.buttons = [Button(p) for p in btn_pins]
        
        # ADC (Knobs/CVs)
        self.cv_a = Knob(cv_pin_a)
        self.cv_b = Knob(cv_pin_b)
        
        # Calibration object
        self.calibration = calibration
        
    def scan_buttons(self):
        """
        Returns index of pressed button or -1.
        """
        for i, btn in enumerate(self.buttons):
            if btn.was_pressed():
                return i
        return -1

    def read_cv(self, channel='A'):
        """
        Returns input as a float Note Number (e.g. 60.0 = C4).
        """
        # use Knob class for smoothed reading
        knob = self.cv_a if channel == 'A' else self.cv_b
        raw = knob.read_u16()
        
        # Use calibration object if available
        if self.calibration:
            return self.calibration.adc_to_note(raw)
        
        # Fallback to defaults
        # Default: 12000 raw units per volt, 0V = Note 24
        volts = raw / 12000.0
        return 24 + (volts * 12)
