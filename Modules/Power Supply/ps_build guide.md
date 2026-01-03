# Dual Rail Power Supply Build Guide

## Overview
This module is the heart of your system. It takes 12V AC from a wall wart and converts it into the stable **+12V** and **-12V** DC power that Eurorack modules need.

> [!WARNING]
> **POLARITY MATTERS!**
> Unlike the passive attenuator, this circuit has specific orientations.
> - **Capacitors** have a stripe (-) side.
> - **Diodes** have a stripe (Cathode).
> - **Regulators** must not be swapped (7812 is NOT the same as 7912).
> **Double-check every step.** A mistake here can damage other modules.

---

## 1. Bill of Materials (BOM)

| Component | Value/Part | Quantity | Notes |
| :--- | :--- | :--- | :--- |
| **P1** | 12V AC Wall Wart | 1 | **Must be AC Output**, not DC! (Not included in component bags) |
| **J1** | 2.1mm DC Socket | 1 | Pro Signal PS11599 (Panel Mount) |
| **D1, D2** | 1N4001 | 2 | Rectifier Diodes (Black with silver band) |
| **C1, C3** | 2200µF 25V | 2 | Large Electrolytic. **Polarized!** |
| **C2, C4** | 100nF (0.1µF) | 2 | Small Ceramic (Yellow/Blue blobs). Non-polarized. |
| **U1** | L7812CV | 1 | +12V Regulator (Positive) |
| **U2** | L7912ACV | 1 | -12V Regulator (Negative) |
| **J2** | Pin Header | 1 | 3-pin Male Header (Output) |
| **Board** | Stripboard | 1 | Cut to size (approx 15x15 holes is plenty) |

---

## 2. Stripboard Layout
We will use a logical layout where the Regulators sit in 3 adjacent rows.
*   **Top Block (Rows 2-4):** Positive Rail (+12V)
*   **Bottom Block (Rows 6-8):** Negative Rail (-12V)

### Graphical ASCII Layout
*(View from Top - Components Side)*

```ascii
         1   2   3   4   5   6   7   8   9   10  11  12
       +---+---+---+---+---+---+---+---+---+---+---+---+
Row 1  | (Unused / Spacing)                            |
       +---+---+---+---+---+---+---+---+---+---+---+---+
Row 2  | AC1---[ D1 >| ]---[ C1+ ]---[ 7812 IN ]-------|
       +---+---+---+---+---|-----|---|---------|---+---+
Row 3  | AC2---(GND)-------[ C1- ]---[ 7812 GD ]-------|-----> GND
       +---+---+---+---+---|-----|---|---------|---+---+
Row 4  |                   [ C2  ]   [ 7812 OT ]-------|-----> +12V
       +---+---+---+---+---+---+---+---|---+---|---+---+
Row 5  | (Wire Link connecting Row 3 to Row 6)         |
       +---+---+---+---+---+---+---+---+---+---+---+---+
Row 6  |                   [ C4  ]   [ 7912 GD ]-------|
       +---+---+---+---+---|-----|---|---------|---+---+
Row 7  | AC1---[ |< D2 ]---[ C3- ]---[ 7912 IN ]-------|
       +---+---+---+---+---|-----|---|---------|---+---+
Row 8  |                   [     ]   [ 7912 OT ]-------|-----> -12V
       +---+---+---+---+---+---+---+---+---+---+---+---+
```

### Key Connections:
1.  **AC1 (Live):**
    *   Connects to **Row 2** (D1 Anode).
    *   ALSO connects to **Row 7** (D2 Cathode). *Use a wire jumper to link Row 2 and Row 7 at Column 2.*
2.  **AC2 (Neutral/Ground):**
    *   Connects to **Row 3** (Ground).
    *   *Note:* Row 3 must be linked to Row 6 to share ground with the negative regulator.
3.  **Polarity Checks:**
    *   **D1:** Band (Cathode) points RIGHT (towards regulators).
    *   **D2:** Band (Cathode) points LEFT (towards AC input).
    *   **C1 (Top Cap):** Positive leg in Row 2, Negative leg in Row 3.
    *   **C3 (Btm Cap):** Positive leg in Row 6 (GND), Negative leg in Row 7 (-V). **Careful here!** The capacitor's stripe (-) goes to the -12V rail (Row 7).

---

## 3. Step-by-Step Assembly

### Step 1: Component Placement
1.  **Diodes:**
    *   **D1 (Row 2):** Input side. Band facing Right.
    *   **D2 (Row 7):** Input side. Band facing Left.
2.  **Links:**
    *   Solder a wire link between **Row 3** and **Row 6** (Ground Link).
    *   Solder a wire link between **Row 2** (Col 1) and **Row 7** (Col 1) to share the AC1 input.
3.  **Capacitors:**
    *   **C1 (2200uF):** + in Row 2, - in Row 3.
    *   **C3 (2200uF):** + in Row 6, - in Row 7. *(Recall: Positive goes to Ground for the negative rail cap).*
    *   **C2 (100nF):** Across Row 3 and 4? *Correction:* C2 is output cap for 7812. Put it between Output (Row 4) and Gnd (Row 3).
    *   **C4 (100nF):** Output cap for 7912. Between Output (Row 8) and Gnd (Row 6).
4.  **Regulators (The Big Ones):**
    *   **7812:** Insert into Rows 2, 3, 4. (In, Gnd, Out).
    *   **7912:** Insert into Rows 6, 7, 8. (Gnd, In, Out).
    *   *Double check names!* 7812 is top. 7912 is bottom.

### Step 2: Wiring
1.  **AC Input:** Solder jack wires to **Row 2** and **Row 3**. (Since Row 2 is linked to Row 7, AC1 goes to both diodes).
2.  **Output:** Solder wires or header to:
    *   **+12V:** Row 4
    *   **GND:** Row 3 (or 6)
    *   **-12V:** Row 8

---

## 4. Connections & Wiring

### Input (J1 - Panel Mount Jack)
1.  Solder two wires to the **AC Input Jack** (polarity doesn't matter for AC).
2.  Twist these wires together to reduce noise.
3.  Connect Wire 1 to **Diode Common Point** (Anode of D1, Cathode of D2).
4.  Connect Wire 2 to **Common Ground** on the board.

### Output (Header)
1.  Solder a 3-pin header to the board.
2.  Use jumper wires on the bottom (or top) to connect:
    *   **Pin 1:** +12V Rail
    *   **Pin 2:** Ground Rail
    *   **Pin 3:** -12V Rail

---

## 5. Testing (Crucial!)

1.  **Safety Check:** Inspect board. Ensure no solder bridges between strips. Ensure capacitors are correct way round (+ to +, - to -).
    *   *Note:* On negative rail, Cap + goes to Ground, Cap - goes to -12V line. This looks "backwards" but is correct for negative voltage.
2.  **Power Up (No Modules):**
    *   Plug in your AC Wall Wart.
    *   Turn on.
3.  **Voltage Check:**
    *   Red Probe on **+12V** pin, Black on **GND**. -> Should read **+11.8V to +12.2V**.
    *   Red Probe on **-12V** pin, Black on **GND**. -> Should read **-11.8V to -12.2V**.
    *   *Note:* If you see -0.5V or +18V, TURN OFF IMMEDIATELY. Check connections.

---
**Congratulations!** You have a Dual Rail Power Supply.
