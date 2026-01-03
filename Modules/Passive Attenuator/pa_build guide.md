# Passive Attenuator: A Learning Build

## Overview
Welcome to your first build. While we *could* just tell you exactly which wire goes where, the goal of Project Bumblebee is for you to **understand** what you are building.

This module is a **Passive Attenuator**. It uses a logic called a **Voltage Divider**.

**Est. Time:** 45 Minutes
**Difficulty:** Beginner (Educational)

---

## 1. The Theory: Voltage Dividers
An attenuator isn't just a "volume knob." It is a circuit that takes an Input Voltage ($V_{in}$) and splits it across two resistances to create a smaller Output Voltage ($V_{out}$).

We use a **Potentiometer** (Pot), which is essentially a variable resistor with a "Wiper" that slides along it.

### The Schematic
Engineers read schematics, not wiring lists. Here is the schematic for what you are building:

```
      (Input Signal)
           |
       [ Pin 3 ]  <-- Top of Resistor
           |
           |   <----- [ Pin 2: Wiper ] ---------> (Output Signal)
           |
       [ Pin 1 ]  <-- Bottom of Resistor
           |
       (Ground / 0V)
```

**How it works:**
*   **Knob CW (Full Volume):** The Wiper slides up to Pin 3. Output is connected directly to Input.
*   **Knob CCW (0 Volume):** The Wiper slides down to Pin 1. Output is connected directly to Ground (Silence).
*   **Knob Middle:** The Wiper is halfway. Half the voltage acts as "friction" (heat), and half goes to output.

---

## 2. The Practical Challenge

### Challenge A: Identify your Nets
In electronics, a "Net" is a group of points that are all connected together. Look at the schematic above. Can you see the 3 Nets?

1.  **The Input Net:** Connects the **Jack Tip (In)** to the **Pot Input (Pin 3)**.
2.  **The Output Net:** Connects the **Pot Wiper (Pin 2)** to the **Jack Tip (Out)**.
3.  **The Ground Net:** Connects **Jack Sleeve (In)** AND **Jack Sleeve (Out)** AND **Pot Ground (Pin 1)**.

### Challenge B: Identify your Pins
Grab your **B100K Potentiometer**.
*   Turn it over so the shaft points **away** from you.
*   Identify Pins 1, 2, and 3.
*   *Hint:* On standard pots (looking from the back), Pin 3 is usually on the LEFT, and Pin 1 is on the RIGHT. (This is often slightly confusing, which is why we verify later!)

---

## 3. The Build Guide (Answer Key)
*Now that you understand the logic, here is the verified step-by-step guide to ensure your build is robust and reliable.*

### BOM & Tools
*   **Jacks:** Pro Signal PS11588
*   **Pot:** 100k Linear (P160KNP)
*   **Wire:** 22 AWG Solid Core

### Step 1: Mechanical Assembly
1.  Mount the Pot and Jacks to the panel.
2.  **Pro Tip:** Rotate the jacks so the Ground Lugs face inwards. This makes connecting the "Ground Net" much easier.

### Step 2: Wiring the "Ground Net"
*Logic: We need a solid reference point for 0V.*
1.  Take your **Solid Core Wire**.
2.  Strip a long piece (or strip sections of it).
3.  Solder it to **Input Jack Sleeve**.
4.  Route it to **Pot Pin 1** (The Rightmost pin when looking from the back). Solder it.
5.  Route it to **Output Jack Sleeve**. Solder it.
    *   *Check:* Do you see how this single wire connects all 3 Ground points?

### Step 3: Wiring the "Input Net"
*Logic: The signal enters the resistor.*
1.  Solder a wire from **Input Jack Tip**.
2.  Connect it to **Pot Pin 3** (The Leftmost pin when looking from the back).

### Step 4: Wiring the "Output Net"
*Logic: The signal leaves via the wiper.*
1.  Solder a wire from **Pot Pin 2** (The Middle pin).
2.  Connect it to **Output Jack Tip**.

---

## 4. Verification (The "Smoke Test")
Before plugging in modules, engineers double-check their logic with a Multimeter.

1.  **Check Ground:** Measure resistance between Input Sleeve and Output Sleeve.
    *   *Expectation:* **~0 Ω**. (If not, your Ground Net is broken).
2.  **Check Function:** Measure resistance between Input Tip and Output Tip while turning the knob.
    *   *Expectation:* Resistance should change from **~100kΩ** (at 0 volume) to **~0Ω** (at Max volume).

### Troubleshooting
*   **Volume works backwards?**
    *   You likely swapped Pin 1 and Pin 3.
    *   *Why?* Because looking from the Front vs Back reverses the orientation. Always double-check your perspective!