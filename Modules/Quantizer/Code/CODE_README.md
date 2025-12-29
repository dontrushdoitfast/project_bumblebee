# Quantizer Code Guide

## Flashing Instructions

1. **Install MicroPython** on your Pico:
   - Hold BOOTSEL, connect USB, drag `.uf2` file to the drive
2. **Copy Files** using Thonny IDE:
   - Copy `main.py` to `/`
   - Copy entire `lib/` folder to `/lib/`
3. **Reset** the Pico to start running

## Calibration (CRITICAL)

The quantizer **must be calibrated** for accurate pitch. Calibration values are stored in `calibration.json`.

### DAC Output Calibration
1. Load `calibration_helper.py` (or modify `main.py` temporarily)
2. Send DAC value `0` → Measure output voltage with multimeter
3. Send DAC value `4095` → Measure output voltage
4. Calculate: `units_per_volt = 4095 / (high_voltage - low_voltage)`
5. Update calibration: `cal.set_dac_scale(units_per_volt * 1/12)` (1V/Oct = 12 semitones)

### ADC Input Calibration
1. Inject exactly **1.00V** into CV In A
2. Read raw ADC value (printed to console)
3. Inject exactly **5.00V**, read raw value
4. Calculate: `adc_per_volt = (raw_5v - raw_1v) / 4.0`
5. Update calibration: `cal.set_adc_scale(adc_per_volt)`

### Quick Test
After calibration, patch the same signal to Input A and Output A (via a mult). 
The quantized output should match the input pitch when playing notes in the scale.

## File Structure
```
/main.py           - Main loop
/lib/
  ├── calibration.py  - Persists DAC/ADC calibration
  ├── scale_logic.py  - Note state & quantization math
  ├── inputs.py       - Button/ADC handling
  └── mcp4725.py      - DAC driver
```

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| No output voltage | I2C not connected | Check SDA/SCL wiring, run I2C scan |
| Wrong pitch | Not calibrated | Follow calibration steps above |
| LEDs not lighting | Wrong data pin | Check GP22 connection to first LED |
| Buttons ignored | Wiring reversed | Buttons should pull LOW when pressed |
| Scale doesn't save | Flash write error | Check free space, try re-flashing |
