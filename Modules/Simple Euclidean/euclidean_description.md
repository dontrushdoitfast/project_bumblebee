# Simple Euclidean Generator

## Overview
The **Simple Euclidean Generator** is an algorithmic rhythm creator. Unlike the "Bernoulli Gate" which relies on randomness, this module relies on **Math**.

It spreads a specific number of "Hits" (beats) as evenly as possible across a 16-step loop. This generates most of the world's musical rhythms (Bossa Nova, Rock, Swing, Techno) automatically.

## Why this module?
1.  **Algorithmic Logic**: It acts as a deterministic counterpoint to the random Bernoulli Gate.
2.  **Instant Groove**: Turn one knob to go from a steady 4/4 kick to a syncopated afro-beat.
3.  **Hardware Identity**: It uses the exact same hardware build as the "Pico Starter / Bernoulli Gate", making it a perfect second project or alternative firmware.

## Features
*   **1 Trigger Input**: Advances the sequencer one step.
*   **Density Knob**: Selects how many hits (1 to 16) are placed in the loop.
*   **2 Trigger Outputs**:
    *   **Out A**: The Euclidean Pattern.
    *   **Out B**: The "Anti-Pattern" (Fires whenever Out A is silent), or Accent? *Currently: Inverse.*
*   **Visual Feedback**: Pico LED flashes on hits.

## Technical Details
*   **Width**: 4HP / 6HP.
*   **Logic**: 3.3V Outputs (Safe for 5V inputs).
*   **Power**: +12V (Regulated to 5V/3.3V).
