# Bumblebee Project Shopping List (UK Edition)

This list aggregates components for the **5 Starter Modules**:
1.  Offset / Attenuverter
2.  CV Mixer
3.  Passive Attenuator
4.  Power Supply
5.  Sequential Switch

## Retailer Strategy (UK)
*   **Specialized Parts (Jacks, Pots, Knobs)**: **Thonk** (Brighton) is the go-to utility player. **Signal Sounds** and **Elevator Sound** are also good but Thonk is dedicated to DIY.
*   **General Components (ICs, Resistors, Caps)**: **Bitsbox** is fantastic for hobbyists (low prices, flat shipping). **Rapid Online** or **Farnell** for bulk/fast ordering. **Tayda** (Asia) is cheaper but allow 2 weeks for delivery (choose "Royal Mail" shipping to avoid fees).
*   **Power**: Wall Wart needs specific attention (AC Output, UK Plug).

---

## 1. Specialized Synth Parts
*Best sourced from [Thonk](https://www.thonk.co.uk/).*

| Component | Quantity Needed | Bulk Buy Recommendation | Est. Price (Each) | Est. Total | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3.5mm Jack** (Thonkiconn PJ-398SM / PJ-301M-12) | 17 | **25 or 50 pack** | ~£0.37 | £9.25 | "Thonkiconn" is the standard. Buy 50 (usually £15-£18). |
| **Potentiometer** (Alpha 9mm Vertical B100K) | 7 | **10 pack** | ~£1.20 | £8.40 | **B100K** (Linear). Round shaft fits Thonk/Davies knobs. |
| **Knobs** (Davies 1900 Clone) | 5 | **10 pack** | ~£0.80 | £4.00 | Ensure shaft size matches pots (6.35mm Round usually). |
| **Power Header** (10-pin Eurorack) | 2 | **10 pack** | ~£0.25 | £2.50 | Male IDC headers (boxed or unboxed). |
| **Power Cable** (10-to-16 pin) | 2 | **5 pack** | ~£2.50 | £12.50 | Ribbon cables. Thonk sells nice ready-made ones. |

**Subtotal: ~£37.00**

### Budget Alternative (AliExpress / Tayda)
*   **Pots**: You can findpacks of "10x B100K 9mm Pots" on AliExpress for ~£3.00.
    *   *Warning*: Shafts are usually "Knurled" (splined), not Round. You will need **Knurled 6mm Knobs** (also cheap on AliExpress, ~£2.00 for 10).
    *   *Shipping*: Takes 2-3 weeks.
*   **Total Savings**: Could save ~£10.00, but quality may vary.

---

## 2. General Electronics (Bitsbox / Rapid)
*Sourced from [Bitsbox.co.uk](https://www.bitsbox.co.uk/).*

| Component | Quantity | Buy Size | Est. Price | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **TL072** (Dual Op-Amp) | 2 | 5 | £0.40 | DIP-8 Package. |
| **CD4017** (Decade Counter) | 1 | 2 | £0.50 | DIP-16. |
| **CD4051** (Analog Mux) | 1 | 2 | £0.50 | DIP-16. |
| **L7812CV** (+12V Regulator) | 1 | 2 | £0.55 | TO-220. |
| **L7912CV** (-12V Regulator) | 1 | 2 | £0.60 | TO-220. |
| **DIP-8 Socket** | 2 | 10 | £0.10 | Always socket your ICs! |
| **DIP-16 Socket** | 2 | 10 | £0.15 | For the 4000 series chips. |
| **Stripboard** (Veroboard) | 4 pcs | 3x Large (100x160mm) | £3.50 | Cut to size. |
| **Breakable Male Headers** | 1 strip | 1 strip (40 pins) | £0.50 | For power supply bus. |

**Subtotal: ~£10.00**

### Passive Components (Bitsbox is great for these)
*   **Resistors (1/4W Metal Film)**:
    *   100k (x9), 1k (x9)
    *   *Recommendation*: Bitsbox Resistor Kit or buy packs of 10 (£0.12/pack).
*   **Capacitors**:
    *   100nF Ceramic (x4) - £0.50 for 10.
    *   10uF Electrolytic (x4) - £0.80 for 10.
    *   2200uF 25V Electrolytic (x2) - £0.60 each.
*   **Diodes**:
    *   1N4004 (x2) - £0.10.
    *   1N4148 (x1) - £0.05.
*   **LEDs**:
    *   3mm Red/Green (x8 total) - £1.00 for mixed bag.

**Passives Subtotal: ~£8.00**

---

## 3. The "Gotchas" (Specific Items)

### 12V AC Power Supply (AC-AC Adapter)
**CRITICAL**: Most UK power bricks are DC. You need **AC Output**.
*   **Spec**: Input 230V, **Output 12V AC**, 1000mA (1A).
*   **Connector**: 2.1mm Barrel Jack.
*   **Sources**:
    *   **eBay UK**: Search "12V AC Power Supply AC-AC 1000mA". Note the "AC-AC" in title. (~£12.00)
    *   **Amazon UK**: Dedicated AC-AC supplies (often hefty transformers). (~£14.00)
    *   *Note*: Avoid "Switching Adapters" if possible as they are often DC. You want a heavy "Linear" transformer if available (rare/expensive now), but any AC output is fine for our rectifier circuit.
*   **Est. Price**: £12.00 - £15.00.

### Barrel Jack & Switch
*   **DC Socket 2.1mm**: Panel mount (Bitsbox Code: CN116). £0.50.
*   **SPST Toggle Switch**: Miniature Toggle (Bitsbox Code: SW031). £0.75.

---

## Grand Total Estimate (UK)
| Category | Estimate |
| :--- | :--- |
| Specialized Parts (Thonk) | £37.00 |
| General Electronics (Bitsbox) | £10.00 |
| Passives | £8.00 |
| Power Supply (Brick) | £15.00 |
| **Total** | **~£70.00** |

*Note: Shipping (Thonk ~£4, Bitsbox ~£2.50) will add slightly to this cost.*
