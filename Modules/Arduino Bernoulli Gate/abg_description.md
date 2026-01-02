# Arduino Bernoulli Gate

## Overview
This module is a **Probability Switch** built on the Arduino platform. It takes an incoming rhythmic trigger (Clock) and flips a coin.
*   **Heads**: The trigger is routed to Output A.
*   **Tails**: The trigger is routed to Output B.

Using the **Probability Knob**, you can bias the coin toss:
*   **0%**: Always B.
*   **50%**: Perfect random distribution.
*   **100%**: Always A.

It is perfect for creating evolving Hi-Hat patterns, randomizing melody streams (if used with S&H), or splitting a single clock into two related rhythms.

## Why Arduino?
*   **5V Logic**: The Arduino runs natively at 5V, meaning we can drive Eurorack 5V gates **directly** without level shifting buffers.
*   **Interrupts**: The ATmega chips have hardware interrupts (Pin 2/3) for ultra-tight timing response.

## Hardware Interface
*   **Width**: 4HP
*   **Inputs**:
    *   **Trig In**: Clock source (0-12V safe via protection).
*   **Outputs**:
    *   **Out A**: 5V Pulse.
    *   **Out B**: 5V Pulse.
*   **Controls**:
    *   **Probability Knob**: Biases the distribution.
    *   **Manual Button**: Manually fires the logic (Simulates Trig In).

## Specifications
*   **Logic Level**: 5V Output.
*   **Trigger Length**: 10ms (Fixed).
*   **Power**: +12V via **10-pin Power Header**. (Regulated to 5V locally).
