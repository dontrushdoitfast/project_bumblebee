# Raspberry Pi Pico Pinout Reference

Master GPIO reference for all Pico-based modules in Project Bumblebee.

## Pin Types
- **ADC**: GP26, GP27, GP28 (Analog inputs ONLY, 0-3.3V)
- **I2C0**: GP0/GP1 or GP8/GP9 (SDA/SCL)
- **I2C1**: GP2/GP3 or GP6/GP7 (SDA/SCL)
- **Digital**: All other GPIOs (Input/Output)

---

## Quantizer Module

```
┌────────────────────────────────────────┐
│           RASPBERRY PI PICO           │
├────────────────────────────────────────┤
│ GP8  (I2C0 SDA) ──► DACs (MCP4725)    │
│ GP9  (I2C0 SCL) ──► DACs (MCP4725)    │
├────────────────────────────────────────┤
│ GP26 (ADC0) ◄── CV Input A (scaled)   │
│ GP27 (ADC1) ◄── CV Input B (scaled)   │
├────────────────────────────────────────┤
│ GP10-GP21 ◄── Piano Buttons (12x)     │
│   GP10=C, GP11=C#, GP12=D ... GP21=B  │
├────────────────────────────────────────┤
│ GP22 ──► NeoPixel Data (12x PL9823)   │
└────────────────────────────────────────┘
```

| Function | GPIO | Notes |
|----------|------|-------|
| I2C SDA | GP8 | Shared by both DACs |
| I2C SCL | GP9 | Shared by both DACs |
| CV In A | GP26 | ADC0, requires 10V→3.3V scaling |
| CV In B | GP27 | ADC1, requires 10V→3.3V scaling |
| Buttons | GP10-21 | PULL_UP, active LOW |
| LEDs | GP22 | NeoPixel data out |

---

## Clock Generator Module

```
┌────────────────────────────────────────┐
│           RASPBERRY PI PICO           │
├────────────────────────────────────────┤
│ GP0  (I2C0 SDA) ──► LCD 2004          │
│ GP1  (I2C0 SCL) ──► LCD 2004          │
├────────────────────────────────────────┤
│ GP26 (ADC0) ◄── Master BPM Knob       │
│ GP27 (ADC1) ◄── Channel Edit Knob     │
│ GP28 (ADC2) ◄── Option Edit Knob      │
├────────────────────────────────────────┤
│ GP9  ◄── Clock Input (protected)      │
│ GP16 ◄── Channel Select Button        │
│ GP17 ◄── Option Select Button         │
│ GP10-12 ◄── Rotary Encoder (A/B/Sw)   │
├────────────────────────────────────────┤
│ GP2  ──► Clock Out 1 (via buffer)     │
│ GP3  ──► Clock Out 2 (via buffer)     │
│ GP4  ──► Clock Out 3 (via buffer)     │
│ GP5  ──► Clock Out 4 (via buffer)     │
├────────────────────────────────────────┤
│ GP13 ──► LED: Out 2 Selected          │
│ GP14 ──► LED: Out 3 Selected          │
│ GP15 ──► LED: Out 4 Selected          │
│ GP6  ──► LED: Swing Selected          │
│ GP7  ──► LED: Euclid Selected         │
│ GP8  ──► LED: Jitter Selected         │
└────────────────────────────────────────┘
```

| Function | GPIO | Notes |
|----------|------|-------|
| I2C SDA (LCD) | GP0 | |
| I2C SCL (LCD) | GP1 | |
| Master Knob | GP26 | ADC0 |
| Chan Knob | GP27 | ADC1 |
| Opt Knob | GP28 | ADC2 |
| Clock In | GP9 | Protected: 1k + Zener |
| Chan Button | GP16 | PULL_DOWN |
| Opt Button | GP17 | PULL_DOWN |
| Encoder | GP10-12 | A, B, Switch |
| Clock Outs | GP2-5 | Via CD4050 buffer |
| Chan LEDs | GP13-15 | Out 2/3/4 indicators |
| Opt LEDs | GP6-8 | Swing/Euclid/Jitter |

---

## Pin Conflict Check

When designing new Pico modules, avoid these reserved pins:
- **GP26-28**: ADC only (cannot drive LEDs)
- **GP0-1 / GP8-9**: Often used for I2C
- **VSYS**: 5V input only
- **3V3_EN**: Do not use as GPIO
