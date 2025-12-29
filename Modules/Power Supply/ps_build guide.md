# Power Supply Build Guide

### Overview
**WARNING: POWER ELECTRONICS.** While 12V is generally safe to touch, shorts can cause fires or explode components. Double-check all polarities (especially capacitors) before powering on. 

This build uses a **Stripboard** (Veroboard) converting standard schematic logic into linear tracks. You will need to "cut" traces to break connections.

### Tools needed
*   **Soldering Iron** & Solder
*   **Multimeter** (ESSENTIAL)
*   **Track Cutter** (or a drill bit) to break stripboard tracks.
*   **Wire Strippers**
*   **Desoldering Pump** (Mistakes happen).

### Bill Of Materials
*   **1x** Stripboard (approx 20 rows x 20 columns minimum).
*   **1x** 12V AC Wall Wart (1000mA). **MUST BE AC OUTPUT.**
*   **1x** PJ-002A (or compatible) 2.1mm Barrel Jack (Panel Mount).
*   **1x** SPST Toggle Switch (Panel Mount).
*   **Power Components**:
    *   **1x** L7812CV (+12V Regulator).
    *   **1x** L7912CV (-12V Regulator). *Note: Different pinout to 7812!*
    *   **2x** 2200uF 25V Electrolytic Capacitors (Unpolarized is OK, but Polarized usually standard).
    *   **2x** 10uF 25V Tantalum/Electrolytic Capacitors (for regulator stability).
    *   **2x** 1N4004 (or 1N4001) Diodes (Rectifiers).
*   **Indicators**:
    *   **2x** 3mm LEDs (Green/Red).
    *   **2x** 1k Resistors (Current limiting for LEDs).
*   **Connection**:
    *   1x 16-pin Male Header (for Bus cable).
    *   Pin headers or terminal blocks for wiring panel components.

### Schematic / Wiring Diagram
**Logic**:
1.  **AC Input** enters via Jack -> One leg goes to Switch -> Circuit.
2.  **Rectification**: Two diodes split the AC wave. 
    *   D1 (Forward) creates positive raw voltage.
    *   D2 (Reverse) creates negative raw voltage.
3.  **Filtering**: Large caps (2200uF) smooth the raw pulses into DC ripple.
4.  **Regulation**: 
    *   L7812 keeps positive rail at exactly +12V.
    *   L7912 keeps negative rail at exactly -12V.

**Stripboard Layout Concept**:
*(User to find a standard "Dual Half Wave PSU Stripboard" layout. Verified common layouts include 'Frequency Central's Dual Microbus' or similar generic DIY designs.)*

### Step By Step guide

#### Phase 1: Breadboard Prototyping
**CRITICAL**: Build this on a breadboard first to verify your Wall Wart is actually AC and your regulators work.
1.  Connect Wall Wart to Jack. Measure output of Jack with Multimeter (AC Volts). Should be ~12-14V AC.
2.  Build just the Positive side: Diode -> Capacitor -> Input of 7812.
3.  Measure 7812 Output. Should be steady +12V DC.
4.  Build the Negative side: Reversed Diode -> Capacitor (Reversed!) -> Input of 7912.
5.  Measure 7912 Output. Should be steady -12V DC.

#### Phase 2: Stripboard Assembly
1.  **Prepare Board**: Cut the board to size.
2.  **Cut Tracks**: Use the track cutter to break strips under the ICs (Regulators) so input/output/ground don't short.
3.  **Links**: Solder jumper wires FIRST (e.g., connecting Grounds).
4.  **Components**: Solder minimal height parts first (Diodes, Resistors) -> then Headers -> then Capacitors -> then Regulators.
5.  **Heatsinks**: Bolt heatsinks to regulators if using them. Ensure they don't touch each other!

#### Phase 3: Panel Wiring
1.  Mount Jack, Switch, and LEDs to 3D printed faceplate.
2.  Wire Jack -> Switch -> Stripboard AC Input.
3.  Wire Stripboard +12V/-12V/GND -> LEDs (via resistors).

### Troubleshooting
*   **Hum/Buzz**: Capacitor values too low or bad solder joint on filter caps.
*   **Regulator Hot instantly**: SHORT CIRCUIT. Unplug immediately. Check track cuts.
*   **Output is 0V**: Check fuse (if installed) or Switch wiring.
*   **Negative Rail is Positive**: Capacitor polarity reversed or Diode backward.

### Testing plan
1.  **Visual Inspection**: Check all polarized capacitors. **If backwards, they will explode.**
2.  **Continuity**: Check GND to +12V and GND to -12V pins. Should NOT beep.
3.  **Voltage Check (No Load)**: Power on. Measure Rails.
    *   Red Probe on +12, Black on GND: **+11.8V to +12.2V**.
    *   Red Probe on -12, Black on GND: **-11.8V to -12.2V**.
4.  **Load Test**: Connect a cheap module (or resistor). Monitor voltage sag.
