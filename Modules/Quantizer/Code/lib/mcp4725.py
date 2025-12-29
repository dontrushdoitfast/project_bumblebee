
import machine

class MCP4725:
    """
    Driver for MCP4725 12-bit DAC.
    """
    def __init__(self, i2c, address=0x60):
        self.i2c = i2c
        self.address = address
        self.max_val = 4095
        # Buffer for I2C writes (2 bytes for Fast Mode)
        # Byte 1: (0 0 0 0 D11 D10 D9 D8) - 4 MSB bits
        # Byte 2: (D7 D6 D5 D4 D3 D2 D1 D0) - 8 LSB bits
        self._write_buf = bytearray(2)

    def write(self, value):
        """
        Write a 12-bit value (0-4095) to the DAC.
        """
        if value < 0:
            value = 0
        elif value > self.max_val:
            value = self.max_val
            
        # Fast Write Command logic
        # First byte: 4 upper bits of data
        self._write_buf[0] = (value >> 8) & 0x0F
        # Second byte: 8 lower bits of data
        self._write_buf[1] = value & 0xFF
        
        try:
            self.i2c.writeto(self.address, self._write_buf)
        except OSError:
            # Handle I2C errors silently or log? In eurorack, typically silent fail or retry is better than crashing loop
            pass
