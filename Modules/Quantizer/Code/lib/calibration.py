
import json

class Calibration:
    """
    Persists DAC and ADC calibration values to flash.
    Prevents users from needing to edit code after calibration.
    """
    def __init__(self, settings_file='calibration.json'):
        self.settings_file = settings_file
        
        # Defaults (reasonable starting points, MUST be calibrated)
        # DAC: ~68 units per semitone assuming 3.3V ref, 1V/Oct
        self.dac_units_per_semitone = 68.25
        # ADC: ~12000 raw units per volt (after 10V->3.3V divider)
        self.adc_units_per_volt = 12000.0
        # Base note: 0V = MIDI note 24 (C1)
        self.base_note = 24
        
        self.load()
    
    def load(self):
        """Load calibration from flash."""
        try:
            with open(self.settings_file, 'r') as f:
                data = json.load(f)
                self.dac_units_per_semitone = data.get("dac_units_per_semitone", self.dac_units_per_semitone)
                self.adc_units_per_volt = data.get("adc_units_per_volt", self.adc_units_per_volt)
                self.base_note = data.get("base_note", self.base_note)
                print("Calibration loaded:", data)
        except (OSError, ValueError):
            print("No calibration found, using defaults. CALIBRATION RECOMMENDED.")
    
    def save(self):
        """Save calibration to flash."""
        try:
            data = {
                "dac_units_per_semitone": self.dac_units_per_semitone,
                "adc_units_per_volt": self.adc_units_per_volt,
                "base_note": self.base_note
            }
            with open(self.settings_file, 'w') as f:
                json.dump(data, f)
            print("Calibration saved.")
        except OSError as e:
            print("Calibration save failed:", e)
    
    def set_dac_scale(self, units_per_semitone):
        """Set DAC units per semitone and save."""
        self.dac_units_per_semitone = units_per_semitone
        self.save()
    
    def set_adc_scale(self, units_per_volt):
        """Set ADC raw units per volt and save."""
        self.adc_units_per_volt = units_per_volt
        self.save()
    
    def note_to_dac(self, midi_note):
        """Convert MIDI note number to DAC value."""
        val = int((midi_note - self.base_note) * self.dac_units_per_semitone)
        return max(0, min(4095, val))
    
    def adc_to_note(self, raw_adc):
        """Convert raw ADC reading to MIDI note number (float)."""
        volts = raw_adc / self.adc_units_per_volt
        # 1V/Oct = 12 semitones per volt
        return self.base_note + (volts * 12)
