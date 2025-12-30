from machine import ADC, Pin
import time

MAX_UINT16 = 65535

class Knob:
    def __init__(self, pin_id):
        self.adc = ADC(Pin(pin_id))

    def percent(self):
        """Return 0.0 to 1.0"""
        return self.adc.read_u16() / MAX_UINT16

    def range(self, steps):
        """Return 0 to steps-1"""
        val = int(self.percent() * steps)
        return min(val, steps - 1)

class Button:
    def __init__(self, pin_id, debounce_ms=50):
        self.pin = Pin(pin_id, Pin.IN, Pin.PULL_DOWN)
        self.debounce_ms = debounce_ms
        self.last_press = 0

    def is_pressed(self):
        return self.pin.value() == 1

    def was_pressed(self):
        """Returns True if pressed significantly (debounced)"""
        if self.pin.value() == 1:
            now = time.ticks_ms()
            if time.ticks_diff(now, self.last_press) > self.debounce_ms:
                self.last_press = now
                return True
        return False
