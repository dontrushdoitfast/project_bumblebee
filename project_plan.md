# Project Bumblebee Build Plan

## Overview
This plan organizes the build into two stages.
*   **Stage 1:** Focuses on essential utilities, logic, power, and the critical "Bridge" to your DAW.
*   **Stage 2:** Completes the system with advanced timing, pitch quantization, and mixing.

**User Inventory Note:**
*   You already possess: **Arduino Uno** (Clone) + **LCD Display**.
*   *Note*: The Arduino Uno is physically large. It is perfect for the "Bernoulli Gate" prototype, but fitting it into a 4HP Eurorack case is difficult. I recommend prototyping with the Uno, but ultimately swapping to an Arduino Nano (~£4) for the final rack mounting.

---

## Stage 1: The Core & The Bridge
**Goal**: Get power running, learn to solder, build basic rhythm logic, and link to Logic Pro.

### Modules
1.  **Passive Attenuator** ("Hello World" Build)
2.  **Power Supply** (Infrastructure)
3.  **Arduino Bernoulli Gate** (Logic/Probability)
4.  **Simple Euclidean** (Rhythmic Logic)
5.  **Sequential Switch** (1 Unit) (Routing)
6.  **[PURCHASE] Behringer CM1A** (Replaces "The Bridge")
    *   *Why*: £33 gets you 16-bit precision and immediate MIDI-CV. Hard to beat DIY price/performance here.

### Stage 1 Bill of Materials (BOM)

#### 1. Specialized Parts (Sourcing: Thonk / Synthcube)
| Component | Quantity | Notes | Est. Cost |
#### 1. Specialized Parts (Sourcing: Thonk / Synthcube)
| Component | **Min Needed Now** | **Smart Buy** | Notes |
| :--- | :---: | :---: | :--- |
| **3.5mm Jacks** (PJ-301M-12) | **15** | **70** | 4(Atten) + 1(PSU) + 3(ABG) + 3(Euc) + 4(Switch). Buying 70 covers Stage 2. |
| **Potentiometers** (B100k) | **4** | **30** | 2(Atten) + 1(ABG) + 1(Euc). 30 covers Stage 2. |
| **Knobs** (To fit Pots) | **4** | **25** | Only 4 needed for Stage 1. |
| **Tactile Buttons** | **2** | **10** | 1(ABG) + 1(Euc). |
| **Power Header (PSU)** | **1** | **1** | **16-pin Male Header** (Boxed/Keyed). Solder to PSU board. |
| **Power Header (Modules)** | **4** | **12** | **10-pin Male Header** (Unboxed/Break-away). Solder to Module boards. |
| **Flying Bus Cable** | **1** | **1** | **Male Flying Bus Cable (Long - 60cm)**. Connects to PSU Header. |
| **Module Power Cables** | **5** | **10** | **"10-16 Pin Power Cable"** (Short - 15cm). Connects modules to Bus. |
| **SPST Switch** | **1** | **1** | For PSU. |
| **DC Barrel Jack** | **1** | **1** | Panel Mount (2.1mm). |

#### 1a. Tools & Equipment (Essential for Stage 1)
*(Quantities are always 1 unless specified)*
| Tool | Note | Est. Cost |
| :--- | :--- | :--- |
| **Soldering Iron** | Adjustable temperature recommended. | ~£20+ |
| **Multimeter** | Essential for safety checks. | ~£15 |
| **Track Cutter** | Or a 3mm Drill Bit (for breaking stripboard tracks). | ~£4 |
| **Veroboard / Stripboard** | Buy large sheets (e.g. 100x160mm) and cut to size. | ~£10 |
| **Wire Strippers & Cutters** | | ~£10 |
| **Desoldering Pump** | For inevitable mistakes. | ~£5 |

#### 2. Chips & Microcontrollers (Sourcing: Bitsbox / Mouser)
| Component | **Min Needed Now** | **Smart Buy** | Notes |
| :--- | :---: | :---: | :--- |
| **Raspberry Pi Pico** | **1** | **2** | 1 for Euclidean. Smart Buy adds 1 Spare. |
| **Arduino Nano** | **1** | **1** | For Bernoulli Gate. |
| **CD4017** | **1** | **2** | 1 for Switch. Smart Buy adds 1 Spare. |
| **CD4051** | **1** | **2** | 1 for Switch. Smart Buy adds 1 Spare. |
| **TL072** | **0** | **10** | None needed for Stage 1! Used in Stage 2. |
| **L7812 + L7912** | **1 set** | **2 sets** | 1 for PSU. Smart Buy adds Spare Set. |
| **IC Sockets** (DIP-16) | **2** | **10** | For CD4017/CD4051. |
| **Pico/Nano Headers** | **1 set** | **10 sets** | 20-pin (Pico) + 15-pin (Nano) Female Headers. |

#### 3. General Components (Sourcing: Bitsbox)
*   **Resistors** (**SMART BUY** - Buy Packs of 100):
    *   100k (Input Modulation)
    *   1k (Output Protection)
    *   10k / 39k (Small packs OK)
*   **Capacitors**:
    *   2200uF 25V (x2) (PSU Main)
    *   10uF (x10) (Local bypass)
    *   100nF (**SMART BUY** - Buy Pack of 50/100) (Decoupling)
*   **Diodes**:
    *   1N4004 (x2) (PSU)
    *   1N4148 (**SMART BUY** - Buy Pack of 50) (Switch Logic + General)
    *   1N5817 (x2) (Pico Inputs)
*   **Transistors**:
    *   2N3904 (x1) (Switch Clock)
*   **LEDs**:
    *   ~6 (Indicators)
*   **Stripboard**: 2-3 large sheets.

**Est. Stage 1 Total: ~£60 - £75** (Plus Wall Wart if needed)

---

## Stage 2: Expansion & Pitch Control
**Goal**: Complete the system with advanced timing, pitch quantization, and mixing.

### Modules
1.  **Clock Generator** (The Brain) - *Uses your LCD*
2.  **Quantizer** (Pitch Correction)
3.  **CV Mixer** (x2)
4.  **Offset / Attenuverter** (x2)
5.  **Simple Delay**
6.  **Dual Linear VCA**
7.  **Buffered Mult**
7.  **Buffered Mult**
8.  *(Remaining Sequential Switch if 2 desired later)*
9.  **The Bridge** (Moved to Phase 2: If you want to learn DACs/Coding later)

### Stage 2 Bill of Materials (Approximate)
*   **Jacks**: ~45
*   **Pots**: ~24
*   **Knobs**: ~24
*   **Switches**: 12 (Tactile for Quantizer)
*   **Chips**:
    *   Raspberry Pi Pico (x2) (Clock, Quantizer)
    *   TL072 / TL074 (x6+) (Mixers, VCA, Mult, Quantizer)
    *   LM13700 (x1) (VCA)
    *   PT2399 (x1) (Delay)

**Est. Stage 2 Total: ~£120**

---

## Sourcing Recommendations (UK)

1.  **Thonk (Brighton)**:
    *   *Buy*: Jacks (Thonkiconn), Pots (Alpha 9mm), Power Cables, Knobs.
    *   *Why*: Best quality, specialized for Audio/Eurorack.

2.  **Bitsbox (Online)**:
    *   *Buy*: Resistors, Caps, Diodes, TL072/CD40xx Chips, Stripboard.
    *   *Why*: Excellent prices for hobbyist quantities, flat shipping.

3.  **Amazon / eBay / Pimoroni**:
    *   *Buy*: Raspberry Pi Picos, Arduino Nano.
    *   *Buy*: 12V **AC** Wall Wart (Search "12V AC Power Supply 1000mA").

### Critical Purchase for Stage 1
**The Wall Wart (AC Adapter)**
*   You MUST buy an **AC Output** adapter. Most laptop chargers are DC.
*   Search for: "AC to AC Adapter 12V".
