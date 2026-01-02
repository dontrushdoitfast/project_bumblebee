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
#### 1. Mechanical & Interface (Source: CPC Farnell)
| Component | **Min Needed Now** | **Smart Buy** | Notes |
| :--- | :---: | :---: | :--- |
| **3.5mm Jacks** (Panel Mount) | **15** | **50+** | Generic "Chassis Mount" Mono Sockets. |
| **Potentiometers** (16mm) | **4** | **20+** | **B100K Linear**. Solder lugs are easier for air-wiring. |
| **Knobs** (To fit 16mm Pots) | **4** | **20+** | Ensure shaft size matches Pot (usually 6mm Round or 6.35mm). |
| **Tactile Buttons** | **2** | **10** | Standard 6x6mm or Panel Mount variants. |
| **Power Header (PSU)** | **1** | **1** | **16-pin Male Header** (Boxed). Solder to PSU board. |
| **Power Header (Modules)** | **4** | **12** | **10-pin Male Header**. Solder to Module board. |
| **Ribbon Cable** | **1 meter** | **Rainbow (10+ way)** | For clean connections between Panel <-> Logic Board. |
| **Solid Core Wire** | **1 spool** | **22 or 24AWG** | For Stripboard links, jumpers, and Ground Bus wiring. |
| **SPST Switch** | **1** | **1** | For PSU (Panel Mount Toggle). |
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
| **Helping Hands** | A stand with clips to hold parts while soldering. | ~£8 |

#### 2. Chips & Microcontrollers (Sourcing: Bitsbox / Mouser / Amazon)
**STATUS: ORDERED (2026-01-02)**
*   **NOTE**: You purchased a **Behringer CM1A** (MIDI to CV). This effectively acts as "The Bridge" for now, allowing you to control the rack from your DAW immediately.
*   **Raspberry Pi Pico H**: 2x Received.

#### 3. Missing / To-Source Items (Critical Check)
#### 3. Missing / To-Source Items (Critical Check)
*   **Patch Cables**: You still need **3.5mm mono patch cables** to patch modules together. You won't be able to patch a signal without these!

#### 4. Resolved / Ordered Items
*   **Power Supply Rectifier Diodes**: 100x 1N4001 (Amazon). **Status: ORDERED**.
*   **Power Cables**: 5x 30cm Eurorack Cables (Amazon). **Status: ORDERED**.
| Component | **Min Needed Now** | **Smart Buy** | Notes |
| :--- | :---: | :---: | :--- |
| **Raspberry Pi Pico H** | **1** | **2** | **"H" version means pre-soldered pins.** Saves time and risk. |
| **Arduino Nano** | **1** | **1** | For Bernoulli Gate. |
| **CD4017** | **1** | **2** | 1 for Switch. Smart Buy adds 1 Spare. |
| **CD4051** | **1** | **2** | 1 for Switch. Smart Buy adds 1 Spare. |
| **TL072** | **0** | **10** | None needed for Stage 1! Used in Stage 2. |
| **L7812 + L7912** | **1 set** | **2 sets** | **TO-220 Package (1.5A version).** Avoid "L" variants for the main PSU. |
| **IC Sockets** (DIP-16) | **2** | **10** | For CD4017/CD4051. |
| **Female Headers** | **1 set** | **10 sets** | **20-pin strips**. Needed on stripboard to "plug in" the Pico. |

#### 3. General Components (Style: Through-Hole / Axial)
*   **Resistor & Diode Kit** (**SMART BUY**): **Miuzei 1475pcs Assortment Kit** (~£12 on Amazon).
    *   *Includes*: 1/4W 1% Metal Film Resistors (all needed values) + 50 Rectifier Diodes.
    *   *Why*: Neatly labeled and covers Stage 1 AND Stage 2 for less than buying individual packs.
*   **Capacitors** (**Min 25V Rating**):
    *   **2200uF Electrolytic** (x2) (PSU Main)
    *   **10uF Electrolytic** (x20) (Local decoupling - SMART BUY pack)
    *   **100nF Ceramic MLCC** (x50) (Essential - SMART BUY pack)
*   **Transistors**: **2N3904** (x10) (TO-92 Package).
*   **LEDs**: ~10 (5mm Diffuse Indicators - recommended for visibility).
*   **Stripboard**: **FR2 / Epoxy Paper** (Easier to cut by hand).
    *   Search CPC for **E003** (160x100mm) or **E011** (500x100mm).

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

1.  **CPC Farnell (UK)**:
    *   **Recommended For**: EVERYTHING (if possible).
    *   *Why*: Professional industrial supplier, huge range, reliable.
    *   *Search Tips*:
        *   **Pots**: Search "Potentiometer Rotary Linear 100k 16mm" (Look for TT Electronics / ALPS).
        *   **Knobs**: Search "Knob 6mm shaft" (Generic push-fit or set screw).
        *   **Jacks**: Search "3.5mm Mono Chassis Socket" (Look for Lumberg or Pro Signal).
        *   **Switches**: Search "Toggle Switch SPST" or "Tactile Switch 6x6mm".
        *   **Components**: Resistors, Caps, Chips (TI/ST brands).
    *   *Note*: Minimum order for free shipping is usually ~£20.

2.  **Amazon / eBay / Pimoroni**:
    *   *Buy*: Raspberry Pi Picos, Arduino Nano.
    *   *Buy*: 12V **AC** Wall Wart (Search "12V AC Power Supply 1000mA").

### Critical Purchase for Stage 1
**The Wall Wart (AC Adapter)**
*   You MUST buy an **AC Output** adapter. Most laptop chargers are DC.
*   Search for: "AC to AC Adapter 12V".
