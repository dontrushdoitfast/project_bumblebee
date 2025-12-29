
import json
import uos
import utime

# Note Names for reference
NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

class ScaleLogic:
    """
    Manages active keys (scale) and quantization logic.
    Handles persistence to settings.json.
    """
    def __init__(self, settings_file='settings.json'):
        self.settings_file = settings_file
        # Default to C Major
        # C, C#, D, D#, E, F, F#, G, G#, A, A#, B
        # T, F,  T, F,  T, T, F,  T, F,  T, F,  T
        self.active_notes = [True, False, True, False, True, True, False, True, False, True, False, True]
        self.last_save_time = 0
        self.dirty = False
        
        self.load()

    def load(self):
        try:
            with open(self.settings_file, 'r') as f:
                data = json.load(f)
                if "active_notes" in data and len(data["active_notes"]) == 12:
                    self.active_notes = data["active_notes"]
                    print("Loaded Scale:", self.active_notes)
        except (OSError, ValueError):
            print("No settings found or corrupt, using default (C Major).")

    def save(self):
        """Saves current state to flash."""
        try:
            with open(self.settings_file, 'w') as f:
                json.dump({"active_notes": self.active_notes}, f)
            print("Settings saved.")
            self.dirty = False
        except OSError as e:
            print("Save failed:", e)

    def toggle_note(self, note_index):
        if 0 <= note_index < 12:
            self.active_notes[note_index] = not self.active_notes[note_index]
            self.dirty = True
            
            # Safety: Ensure at least one note is on
            if not any(self.active_notes):
                self.active_notes[note_index] = True # Revert

    def check_autosave(self):
        """Call this in the main loop to handle lazy saving."""
        if self.dirty:
            # Simple logic: Save if it's been dirty for a while? 
            # Or just save immediately on button press but with cooldown?
            # Let's enforce a cooldown in the main loop instead.
            pass

    def quantize(self, raw_note_number):
        """
        Takes a float note number (e.g. 60.4 for Middle C + slight sharp).
        Returns the nearest MIDI Note Number that is active in current scale.
        """
        base_octave = int(raw_note_number // 12)
        fractional_note = raw_note_number % 12
        
        # Find nearest active note in this octave
        closest_note = -1
        min_dist = 99.0
        
        # Check all 12 notes in loop
        for i in range(12):
            if self.active_notes[i]:
                # Distance in semitones (circular? No, simple linear is fine for CV)
                # But wait, logic: If we are at C (0.1) and B (11) is active but C is not,
                # we should snap down to B of previous octave (-1) or up to D (2).
                
                # Simple "Snap" approach:
                # 1. Round fractional_note to nearest integer
                # 2. Search outwards from there for nearest active note
                pass
        
        # Simpler approach: Brute force distance check against all active notes in 3 octaves? No, slow.
        # Optimized approach:
        
        target_int = int(round(fractional_note))
        
        # Search Up
        up_dist = 0
        found_up = -1
        for i in range(12):
            idx = (target_int + i) % 12
            if self.active_notes[idx]:
                found_up = idx
                up_dist = i
                break
                
        # Search Down
        down_dist = 0
        found_down = -1
        for i in range(12):
            idx = (target_int - i + 12) % 12
            if self.active_notes[idx]:
                found_down = idx
                down_dist = i
                break
        
        # Compare
        final_note_index = 0
        offset = 0
        
        if up_dist <= down_dist:
            final_note_index = found_up
            if found_up < target_int: # Wrapped into next octave
                offset = 12
        else:
            final_note_index = found_down
            if found_down > target_int: # Wrapped into prev octave
                offset = -12
                
        return (base_octave * 12) + final_note_index + (1 if (found_up < target_int and up_dist <= down_dist) else 0) - (1 if (found_down > target_int and down_dist < up_dist) else 0)
        
        # WAIT, simpler logic:
        # Just generate a list of all valid MIDI notes (0-120) based on active_notes
        # Then find the closest value in that list to raw_note_number.
        # Efficient? We can cache it.
        
    def get_closest_note(self, raw_note):
        """
        More robust implementation.
        """
        # Find closest integer
        target = int(round(raw_note))
        
        # Search for closest active note
        for dist in range(12):
            # Check Up
            candidate = target + dist
            if self.active_notes[candidate % 12]:
                return candidate
            
            # Check Down
            candidate = target - dist
            if self.active_notes[candidate % 12]:
                return candidate
        
        return target # Fallback (should never happen if safety ensures 1 note active)
