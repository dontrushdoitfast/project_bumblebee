# Sequential Switch Build Guide

### Overview
This module introduces **Active Electronics** (Integrated Circuits). You will wire a logic chip (4017) to talk to an analog switch (4051). Precision is key here; a single misplaced wire on the breadboard means it won't work.

### Tools needed
*   **Soldering Iron**, Solder, Cutters, Strippers.
*   **Multimeter** (Logic debugging: 0V vs 5V).
*   **Breadboard** (Essential for logic validation).

### Bill Of Materials
Note: we want 2 of these. So double the parts below.

*   **ICs**:
    *   **1x** CD4017BE (Decade Counter). **(Plus 16-pin DIL Socket)**.
    *   **1x** CD4051BE (8-Channel Analog Mux/Demux). **(Plus 16-pin DIL Socket)**.
*   **Jacks**:
    *   **7x** 3.5mm Mono Jacks (Panel Mount).
*   **LEDs**:
    *   **4x** 5mm LEDs (Color of choice).
    *   **4x** 1k Resistors (Current limiting).
*   **Logic Helpers**:
    *   **1x** 2N3904 NPN Transistor (Buffer for Clock input).
    *   **1x** 100k Resistor (Pull-down for Clock).
    *   **1x** 1N4148 Diode (Protection).
*   **Power**:
    *   **1x** 10-pin Male Power Header.

### Schematic / Wiring Diagram

**Circuit Diagram**:
```
   [CLOCK IN]                                              [COMMON I/O]
       │                                                        │
       ▼                                                        ▼
   ┌───────────┐                               ┌────────────────────────────┐
   │ Transistor│                               │         CD4051             │
   │  Buffer   │                               │    (Analog Mux/Demux)      │
   └─────┬─────┘                               │                            │
         │                                     │ VDD(16)=+12V               │
         ▼                                     │ VEE(7)=-12V  ◄─ CRITICAL!  │
   ┌───────────────────┐                       │ VSS(8)=GND                 │
   │      CD4017       │     Diode Logic       │                            │
   │  (Decade Counter) ├─────────────────────► │ A(11), B(10) ◄─Address     │
   │                   │     1N4148 x4         │                            │
   │ CLK(14) ◄─────────┤                       │ OUT 0 ──► [Step 1 Jack]    │
   │ RST(15) ◄── Q4    │                       │ OUT 1 ──► [Step 2 Jack]    │
   │                   │                       │ OUT 2 ──► [Step 3 Jack]    │
   │ Q0──►LED──►Diodes │                       │ OUT 3 ──► [Step 4 Jack]    │
   │ Q1──►LED──►Diodes │                       └────────────────────────────┘
   │ Q2──►LED──►Diodes │
   │ Q3──►LED──►Diodes │
   │ Q4──►RST(15)      │ ◄─ Auto-reset after step 4
   └───────────────────┘
```

**Address Translation (Diode Logic)**:
The CD4017 outputs are "One Hot" (one pin high at a time). The CD4051 expects binary address on A/B pins.
Use 1N4148 diodes to create the address:

| Step | CD4017 Output | A (Pin 11) | B (Pin 10) |
|------|---------------|------------|------------|
| 0    | Q0 High       | 0          | 0          |
| 1    | Q1 High       | 1          | 0          |
| 2    | Q2 High       | 0          | 1          |
| 3    | Q3 High       | 1          | 1          |

*   Q1 and Q3 connect to A via diodes
*   Q2 and Q3 connect to B via diodes

**CD4051 Power (Critical for Bipolar Audio)**:
*   VEE (Pin 7): **-12V** (Must be negative for bipolar audio!)
*   VSS (Pin 8): Ground
*   VDD (Pin 16): +12V

### Step By Step guide

#### Phase 1: Breadboard Logic Check
1.  **Power**: Put CD4017 and CD4051 on board. Power them (+12V/GND, and -12V to 4051 VEE).
2.  **Clock**: Setup the Clock input to step the 4017. Verify with LEDs on 4017 outputs 0-3.
3.  **Reset**: Wire 4017 Pin 10 (Output 4) to Pin 15 (Reset). Verify it loops 4 steps.
4.  **Audio**: Inject Audio into CD4051 Common. Connect Scope/Amp to Output 0.
5.  **Link**: Connect Logic (4017) to Switch (4051) using the Diode Logic method.
6.  **Verify**: Does Audio move from Out 0 -> Out 1 -> Out 2 -> Out 3?

#### Phase 2: Stripboard
*(User to follow standard "Baby 8" or "4-Step Sequencer" stripboard layouts available online, verifying pinouts against datasheets).*

### Troubleshooting
*   **Skips Steps**: Clock signal is noisy. Add a Schmitt Trigger or capacitor to filter input.
*   **Audio Distorts**: Check CD4051 VEE pin. If it's at Ground, negative signals clip. It MUST be at -12V.
*   **Stuck on Step 1**: Reset pin is floating high. Ensure it has a pull-down resistor if using an external reset jack.

### Testing plan
1.  **LED Chase**: Do the lights move?
2.  **Bidirectional Test**: 
    -   Mux Mode: 4 different oscillators in -> 1 output. Does the timbre change every step?
    -   Demux Mode: 1 LFO in -> 4 outputs. Patch outputs to 4 different filter cutoffs. Does the filter dance?
