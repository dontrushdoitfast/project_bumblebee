# Pico Starter: The Bernoulli Gate

## Overview
The **Pico Starter** is designed to be your first foray into using the Raspberry Pi Pico in a Eurorack context. It is a **Bernoulli Gate** (or "Probability Switch").

It takes a single rhythmic input (like a clock or trigger) and flips a digital coin. Based on the "Probability" knob, it routes that trigger to either **Output A** (Heads) or **Output B** (Tails).

This simple utility is musical, useful, and creates interesting, evolving rhythms from static clocks.

## Why this module?
1.  **Low Complexity**: It uses no complex external DACs, ADCs, or op-amps for exact voltage scaling. It is purely digital logic.
2.  **Immediate Gratification**: You plug in a clock, and you get two dancing rhythms out.
3.  **Safe Learning**: It follows the Bumblebee safety standards but keeps the circuit minimal.
4.  **Standard Parts**: Uses the same BOM as the rest of the project (Jacks, Pots, Pico).

## Features
*   **1 Trigger Input**: The source signal to be routed.
*   **Probability Knob**:
    *   **0% (Fully CCW)**: Always Output B.
    *   **50% (Center)**: Random 50/50 chance.
    *   **100% (Fully CW)**: Always Output A.
*   **2 Trigger Outputs**: The resulting signals.
*   **Manual Button**: Manually fire a trigger to test the probability without an input signal.
*   **Visual Feedback**: LEDs on the Pico (or external) to show which output fired.

## Technical Details
*   **Width**: 4HP / 6HP (Easy to fit).
*   **Power**: +12V (Regulated to 5V/3.3V by Pico or onboard regulator).
*   **Logic Level**: 3.3V out (Safe for 5V inputs, standard for Pico Eurorack).
