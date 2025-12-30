# Bumblebee Project Shopping List (UK Edition)

This list aggregates components for **All 8 Modules** (including duplicates where prompted):
1.  **CV Mixer** (x2)
2.  **Clock Generator**
3.  **Offset / Attenuverter** (x2)
4.  **Passive Attenuator**
5.  **Power Supply**
6.  **Quantizer**
7.  **Sequential Switch** (x2)
8.  **Simple Delay**

---

## Retailer Strategy (UK)
*   **Specialized Parts (Jacks, Pots, Knobs)**: **Thonk** (Brighton) is the go-to utility player. **Signal Sounds** and **Elevator Sound** are also good but Thonk is dedicated to DIY.
*   **General Components (ICs, Resistors, Caps)**: **Bitsbox** is fantastic for hobbyists (low prices, flat shipping). **Rapid Online** or **Farnell** for bulk/fast ordering. **Tayda** (Asia) is cheaper but allow 2 weeks for delivery (choose "Royal Mail" shipping to avoid fees).
*   **Power**: Wall Wart needs specific attention (AC Output, UK Plug).

---

## 1. Specialized Synth Parts
*Best sourced from [Thonk](https://www.thonk.co.uk/).*

| Component | Quantity Needed | Bulk Buy Recommendation | Est. Price (Each) | Est. Total | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3.5mm Jack** (Thonkiconn PJ-301M-12) | 46 | **50 pack** | ~£0.35 | £17.50 | 8 (CVM) + 5 (Clk) + 8 (OA) + 4 (Att) + 4 (Qnt) + 14 (SS) + 2 (Dly) + 1 (PSU). |
| **Potentiometer** (Alpha 9mm Vertical B100K) | 22 | **25 pack (or 2x 10 pack)** | ~£1.20 | £26.00 | 6 (CVM) + 3 (Clk) + 8 (OA) + 2 (Att) + 3 (Dly). Linear. |
| **Knobs** (Davies 1900 Clone) | 22 | **25 pack** | ~£0.70 | £17.50 | To match pots. |
| **Power Header** (10-pin Eurorack) | 2 | **10 pack** | ~£0.25 | £2.50 | Male IDC headers (boxed or unboxed). 10-pin ONLY. |
| **Power Cable** (10-to-10 pin) | 2 | **5 pack** | ~£2.50 | £12.50 | Ribbon cables. 10-pin is standard. |
| **Tactile Switches** (6x6mm) | 14 | **20 pack** | ~£0.20 | £4.00 | 12 (Quantizer) + 2 (Clock). |
| **Toggle Switch** (SPST) | 1 | Single | ~£0.75 | £0.75 | For PSU. |

**Subtotal: ~£37.00**

### Budget Alternative (AliExpress / Tayda)
*   **Pots**: You can find packs of "10x B100K 9mm Pots" on AliExpress for ~£3.00.
    *   *Warning*: Shafts are usually "Knurled" (splined), not Round. You will need **Knurled 6mm Knobs** (also cheap on AliExpress, ~£2.00 for 10).
    *   *Shipping*: Takes 2-3 weeks.
*   **Total Savings**: Could save ~£10.00, but quality may vary.

---
## 2. General Electronics (Bitsbox / Rapid)
*Sourced from [Bitsbox.co.uk](https://www.bitsbox.co.uk/).*

| Component | Quantity | Buy Size | Est. Price | Notes |
| :--- | :--- | :--- | :--- | :--- |
    *   **100k** (x30): Buy pack of 100.
    *   **1k** (x30): Buy pack of 100.
    *   **10k, 15k, 22k, 47k**: Small packs.
*   **Capacitors**: ~£5.00
    *   **100nF Ceramic** (x20): Decoupling everywhere.
    *   **10uF Electrolytic** (x10): OA power filtering.
    *   **2200uF 25V** (x2): PSU.
    *   **47uF, 2.2uF**: Delay.
*   **Diodes**: ~£2.00
    *   **1N4148** (x20): SS Logic + Protection.
    *   **1N4004** (x2): PSU.
    *   **3.3V Zener**: Clock protection.
    *   **Schottky**: Quantizer.
*   **LEDs**: ~£3.00
    *   **3mm** (x20): Mixed Red/Green.
    *   **PL9823 / NeoPixel 5mm** (x12): Quantizer.
    *   **Bipolar 3mm** (x4): OA.
*   **Display**: LCD 2004 with I2C Backpack (x1). ~£5.00 (eBay/Amazon).
*   **Encoder**: Rotary Encoder with Push Switch (x1). ~£1.50.

**Passives Subtotal: ~£36.50**

---

## 3. Power Supply Specifics
*   **12V AC Wall Wart**: Input 230V, Output **12V AC** (AC-AC), 1000mA. ~£15.00.
    *   *Note*: Ensure output is AC, not DC.
*   **Barrel Jack**: Panel mount 2.1mm. (Included in specialized parts count, but distinct item).

---

## Grand Total Estimate
| Category | Estimate |
| :--- | :--- |
| Specialized Parts (Thonk) | £93.25 |
| Semiconductors | £24.15 |
| Passives & Misc | £36.50 |
| Power Supply (Brick) | £15.00 |
| **Total** | **~£168.90** |

*Note: This builds a fully functional Eurorack system with 8 modules (11 physical units). Cost per module is approx £15!*
