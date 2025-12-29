import time
from machine import Pin

class ClockCore:
    def __init__(self, out_pins):
        # Hardware
        # [Out1 (Master), Out2, Out3, Out4]
        self.outputs = [Pin(p, Pin.OUT) for p in out_pins] 
        
        # State
        self.bpm = 120
        self.running = True
        self.ppqn = 24  # 24 ticks per quarter note = Standard MIDI resolution
        self.tick_count = 0
        
        # Configuration
        # Divisions: 1 = x1 (Quarter Note), 2 = /2 (Half Note), 4 = /4 (Bar)
        # For now defaults: Master=1, Out2=1, Out3=2, Out4=4
        self.divisions = [1, 1, 2, 4] 
        
        self.last_tick_us = time.ticks_us()
        
        # For Fixed Triggers (Master) logic
        self.trigger_end_times = [0, 0, 0, 0] 

    def set_bpm(self, bpm):
        self.bpm = max(30, min(300, bpm))

    def update(self):
        """Call this in main loop as fast as possible"""
        now = time.ticks_us()
        
        # 1. Handle Trigger Offs (Time-based for Master/Triggers)
        # Only Master (Index 0) is forced Trigger mode currently.
        if self.trigger_end_times[0] > 0:
            if time.ticks_diff(now, self.trigger_end_times[0]) >= 0:
                self.outputs[0].off()
                self.trigger_end_times[0] = 0

        if not self.running: return

        # 2. Check for Next Tick
        # Formula: 60s / BPM / PPQN
        us_per_tick = int((60 * 1000000) / (self.bpm * self.ppqn))
        
        if time.ticks_diff(now, self.last_tick_us) >= us_per_tick:
            self.last_tick_us = now
            self.tick()

    def tick(self):
        # PPQN=24.
        
        # --- MASTER (Index 0) ---
        # Fires every 24 ticks (Quarter Note)
        period_master = 24
        if self.tick_count % period_master == 0:
            self.fire_trigger(0)

        # --- DIVIDERS (Index 1,2,3) ---
        # GATE MODE: 50% Duty Cycle
        for i in range(1, 4):
            div = self.divisions[i]
            period = int(period_master * div)
            
            # Phase: Where are we in the cycle (0 to period-1)
            phase = self.tick_count % period
            
            # Start of Cycle -> HIGH
            if phase == 0:
                self.outputs[i].on()
                
            # Halfway Gate -> LOW
            # e.g. Period 24. High at 0. Low at 12.
            midpoint = period // 2
            if phase == midpoint:
                self.outputs[i].off()

        self.tick_count += 1

    def fire_trigger(self, ch):
        """Fires a short 10ms pulse (Trigger Mode)"""
        self.outputs[ch].on()
        # Schedule OFF in 10ms (10000us)
        self.trigger_end_times[ch] = time.ticks_add(time.ticks_us(), 10000)
