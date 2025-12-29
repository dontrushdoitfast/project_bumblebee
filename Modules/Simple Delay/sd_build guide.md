# Simple Dirty Delay Build Guide

### Overview
This build is slightly more advanced as it combines Op-Amps (Analog) with the PT2399 (Digital) and requires an onboard voltage regulator. You will get comfortable efficiently using stripboard space.

### Tools needed
*   **Soldering Iron** & Solder
*   **Multimeter**
*   **Track Cutter**
*   **Wire Strippers**

### Bill Of Materials
**Note**: This BOM is for ONE Dual-Channel Module (contains 2 delays).

*   **ICs**:
    *   **2x** PT2399 Echo Chips (DIP-16).
    *   **1x** TL074 Quad Op-Amp (DIP-14) (Handles input/output mixing for both channels).
*   **Regulators**:
    *   **1x** L78L05 (TO-92 package) - Small 5V regulator.
*   **Sockets**:
    *   **2x** DIP-16 Sockets.
    *   **1x** DIP-14 Socket.
*   **Potentiometers**:
    *   **6x** B50K or B100K (Linear) - Time, Feedback, Mix.
    *   **6x** Knobs.
*   **Jacks**:
    *   **4x** Thonkiconn PJ-301M-12.
*   **Passives (Per Channel - Multiply by 2)**:
    *   **Resistors**: 10k (x4), 15k (x2), 22k (x2).
    *   **Capacitors**: 100nF (Ceramic), 47uF (Electrolytic), 2.2uF (Electrolytic).
    *   *Note*: The PT2399 requires specific caps for anti-aliasing. A standard "PT2399 datasheet circuit" or "Electrosmash PT2399" schematic is the reference here.
*   **Power**:
    *   **1x** 10-pin Eurorack Header.

### Schematic / Wiring Diagram
**Logic (Per Channel)**:
1.  **Power Creation**: +12V goes into L78L05 -> creates +5V. This Powers Pin 1 of PT2399.
2.  **Input Buffer**: Signal enters TL074 (Stage A).
3.  **Delay Core**: Buffered signal goes into PT2399 (Pin 16).
4.  **Feedback Loop**: Output of PT2399 (Pin 14/15) goes back to Input via a Potentiometer.
5.  **Output Mixer**: Dry Input and Wet Output connect to "Mix" Pot (Crossfader config) -> TL074 (Stage B) -> Output Jack.

### Step By Step guide

#### Phase 1: Breadboard (Single Channel)
1.  **Power**: Setup +12V/-12V. **Add L78L05**. Verify you have stable +5V on the breadboard rail. **Do not feed 12V to the PT2399!**
2.  **IC**: Place PT2399. Power Pin 1 (+5V) and Pins 3/4 (Ground).
3.  **Logic**: Connect the "Time" resistor (Pin 6) and "Feedback" path.
4.  **Audio**: Inject audio. Do you hear echoes?
    *   *Tip*: It usually takes a few tries to get the anti-lockup latchup protection right (Power-on sequence).

#### Phase 2: Stripboard Layout
1.  **Planning**: You need to fit 3 chips (2x PT2399, 1x TL074). This requires a medium/large stripboard (approx 25x25 holes minimum).
2.  **Isolation**: Locate the L78L05 away from the audio path to minimize heat/noise.
3.  **Grounding**: Create a solid ground plane (link multiple tracks) as digital chips are noisy.

#### Phase 3: Panel Wiring
1.  **Mount**: 6 Pots + 4 Jacks is tight. Ensure your faceplate layout allows finger space.
2.  **Wire**: Standard pot wiring.
    *   **Time Pot**: Usually variable resistance to Ground from Pin 6.
    *   **Feedback Pot**: Simple attenuator in the feedback loop.

### Troubleshooting
*   **PT2399 Gets Hot**: You fed it 12V. It is dead. Replace it.
*   **Lock up (Screaming noise on startup)**: The PT2399 is infamous for "latching up". You need a proper power-on reset circuit (usually a small capacitor on the digital ground pin).
*   **Distortion**: Input signal is too hot. The PT2399 runs on 5V, so it clips easily with modular levels (+/-5V). You might need to attenuate the input (via resistor divider) before the chip and amplify it after.

### Testing plan
1.  **Voltage Check**: Verify **Pin 1 of PT2399 is +5V**. If it's 12V, stop.
2.  **Audio Path**: Dry signal passes cleanly?
3.  **Delay**: Turn Mix to Wet. Turn Time. Do pitch shifting artifacts happen? (Good, that's the "Dirty" part).
