# Passive Attenuator Build Guide

### Overview
This is the simplest module in the system, making it perfect for the first build. You will wire two potentiometers and four jacks in a simple "voltage divider" configuration. No circuit board is required; we will use "point-to-point" wiring directly on the components.

### Tools needed
*   **Soldering Iron** & Solder (Lead-free recommended)
*   **Wire Strippers** & Cutters
*   **Multimeter** (for continuity and resistance checks)
*   **Pliers** (for tightening jack nuts)
*   **3D Printer** (Creality K1 Max) & PLA/PETG filament

### Bill Of Materials
*   **4x** **3.5mm Mono Jacks** (Panel Mount) - Generic CPC/Lumberg type.
*   **2x** **100k Linear Potentiometers (16mm)** - High quality, solder-lug terminals.
*   **2x** Knobs (To fit 6mm shaft)
*   **Wire**: 24AWG or 26AWG stranded wire (various colors recommended for Signal vs Ground)
*   **3D Printed Faceplate**: (STL to be generated)

### Schematic / Wiring Diagram
**Wiring Logic (Per Channel)**:
1.  **Grounds**: Connect the Ground (Sleeve) pins of Input Jack, Output Jack, and Potentiometer Pin 1 together. *Note: You can bus all grounds together for simplicity.*
2.  **Input Signal**: Connect Input Jack Tip -> Potentiometer Pin 3.
3.  **Attenuated Signal**: Connect Potentiometer Pin 2 (Wiper) -> Output Jack Tip.

**Visual Representation**:
```
      [In Tip] --------(Pin 3)
                              |
                            [Pot]-----(Pin 2)-----> [Out Tip]
                              |
      [Common GND] ----(Pin 1)
```
*Repeat exactly for Channel B.*

### Step By Step guide

#### Phase 1: Breadboard Prototyping
Before heating up the soldering iron, verify the circuit concept on a breadboard.
1.  **Insert Potentiometer**: Place the B100K pot on the breadboard.
2.  **Connect Input**: Patch a signal (e.g., LFO from Proton) to **Pin 3** (Left outer leg).
3.  **Connect Output**: Patch **Pin 2** (Middle leg/Wiper) to your oscilloscope or mixer.
4.  **Connect Ground**: Connect **Pin 1** (Right outer leg) to the common ground rail.
5.  **Test**: Turn the knob. Ensure the signal fades from Max (CW) to Silent (CCW). If it works, proceed to Phase 2.

#### Phase 2: Final Assembly
1.  **Print the Faceplate**: Slice the 4HP faceplate model in Orca Slicer. Print face-down for the best texture.
2.  **Mount Components**:
    *   Install the 2 potentiometers in the middle holes. Orient terminals facing INWARDS.
    *   Install the 4 jacks. Ensure the ground tabs are accessible.
    *   Tighten all nuts gently (plastic deforms easily).
3.  **Prepare Grounds**:
    *   Cut short lengths of wire to daisy-chain the ground lugs of all 4 jacks and the Pin 1 lug of both pots.
    *   Solder this "ground bus" wire.
4.  **Wire Channel A (Top)**:
    *   Solder a wire from Top Input Jack (Tip) to Top Pot (Pin 3).
    *   Solder a wire from Top Pot (Pin 2/Middle) to Upper-Middle Output Jack (Tip).
5.  **Wire Channel B (Bottom)**:
    *   Repeat the same connections for the bottom set of jacks and pot.
6.  **Final Inspection**: Check for loose wire strands or solder bridges.

### Troubleshooting
*   **No Signal**:
    *   Check that the input signal is actually plugged into the **Input** jack (Top jack of the pair).
    *   Check for "cold" solder joints on the jack lugs.
*   **Reversed Action (Louder when turning Left)**:
    *   You have wired the input to Pin 1 instead of Pin 3. Swap the two outer wires on the potentiometer.
*   **Hum/Noise**:
    *   Check that all ground sleeves are connected together. A missing ground connection causes buzz.


### Testing plan
1.  **Continuity**: Use a multimeter to verify that all Ground points (Jack sleeves, Pot Pin 1) are connected to each other.
2.  **Isolation**: Verify there is NO connection between the Input Tip and Ground (unless Pot is turned).
3.  **Resistance Check**:
    *   Connect Multimeter to Input Tip and Output Tip.
    *   Turn knob fully **CW**: Resistance should be near **0 ohms** (Direct connection).
    *   Turn knob fully **CCW**: Resistance should be near **100k ohms** (Full resistance).
4.  **Functional Test**: Patch audio/CV from the Proton into Input, and Output to your mixer. Verify the knob controls the volume smoothly from Silent to Max.