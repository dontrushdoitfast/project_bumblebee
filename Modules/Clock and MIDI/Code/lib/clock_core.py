import time
from machine import Pin

class ClockCore:
    def __init__(self, out_pins):
        # Hardware
        self.outputs = [Pin(p, Pin.OUT) for p in out_pins] # [Out1, Out2, Out3, Out4]
        
        # State
        self.bpm = 120
        self.running = True
        self.ppqn = 24  # Internal resolution
        self.tick_count = 0
        
        # Configuration [Out1 is Master, fixed at 1]
        self.divisions = [1, 1, 1, 1] # 1=x1, 4=/4, 0.5=x2 (Wait, integer math only first)
        # Using simplified integers: Positive = Division (/X), Negative = Mult (xX)
        self.div_map = [1, 2, 4, 8, 16, 32] # Supported divisions

        self.last_tick = time.ticks_us()
    
    def set_bpm(self, bpm):
        self.bpm = max(30, min(300, bpm))

    def update(self):
        """Call this in main loop as fast as possible"""
        if not self.running: return

        # Calculate time per Tick (Microseconds)
        # 60 sec / BPM / 24 PPQN * 1000000
        us_per_tick = int((60 * 1000000) / (self.bpm * self.ppqn))
        
        now = time.ticks_us()
        if time.ticks_diff(now, self.last_tick) >= us_per_tick:
            self.last_tick = now
            self.tick()

    def tick(self):
        self.tick_count += 1
        
        # Master Output (Out 1) - Fires every 24 ticks (Quarter Note)
        if self.tick_count % 24 == 0:
            self.trigger(0)
            
        # TODO: Implement complex division logic here for Outs 2, 3, 4
        # For prototype: Just mirror Master
        if self.tick_count % 24 == 0:
             self.trigger(1)
             self.trigger(2)
             self.trigger(3)

    def trigger(self, channel_idx):
        self.outputs[channel_idx].on()
        # Note: We need a way to turn them OFF after 10ms. 
        # In a SuperLoop, we check timestamps.
        
