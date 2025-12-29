# Project Bumblebee #



## Background ##

This project creates a set of Eurorack compatible modules to integrate with the current setup. We focus on sequencing and logic to create a full instrument. This came about from frustration with a hybrid setup using Logic Pro to sequence or VCV rack which were too fiddly and ephemeral to set up. The decision was made to create a full sequencing and voicing setup in hardware, rather than jumping back and forth in an unsatisfactory way.

**Primary Equipment**

This is what the modules we create will be primarily used with.

* Behringer 2600 (Grey Meanie)
* Behringer Proton

**Secondary Equipment**

* Thomann the t.mix 16 channel Mixer. Effects sends go to Logic Pro (via an interface)
* iMac with Logic Pro and a USB hub connected to all external instruments for USB midi
* Korg Modwave mk1


## Project Goals


1. Create a set of Eurorack modules to act as a Eurorack brain to integrate with the current setup to create a complete sequenced instrument.
2. Prioritize voltage interaction, routing, and modulation over stored patterns, song modes, or DAW-style sequencing.
3. Learn and implement basic electronics
4. Learn and implement the Raspberry Pi Pico where appropriate
5. Minimise costs to a reasonable level

**Non-goals**

The project will not:

1. Include effects, unless explicitly specified
2. Build menu diving or complex interfaces.
3. Use stored patterns, song modes, or DAW-style sequencing.

## Safety & Testing Protocols

**CRITICAL**: Every new module must be rigorously tested in isolation before being connected to the primary or secondary equipment.

1.  **Smoke Test**: Check for shorts on power rails using a multimeter before powering on.
2.  **Voltage Verification**: Measure all outputs with a multimeter/oscilloscope to ensure they do not exceed safe Eurorack limits (typically +/- 12V absolute max, but aim for standard signal ranges).
3.  **Isolation**: Use the home-made power supply for testing. Do not test untrusted modules on the same bus board as the Behringer 2600.

## Technical Standards

To ensure compatibility with the Behringer 2600, Proton, and standard Eurorack gear:

*   **Signals**:
    *   **Audio**: +/- 5V (10Vpp).
    *   **CV (Bipolar)**: +/- 5V (LFOs, etc.).
    *   **CV (Unipolar)**: 0V to +10V (Envelopes) or 0V to +5V (Pitch/Digital CV).
    *   **Triggers/Gates**: 0V (OFF) to +5V (ON). *Note: The Pico requires buffering to step up 3.3V signals to 5V.*
*   **Power Connectivity**: Standard 10-pin or 16-pin Eurorack power headers.
*   **HP Width**: Integers of 2HP (e.g., 4HP, 6HP, etc.) for easy fitting.

## Phase 1

The following modules are planned for Phase 1 which is the main effort. Phase 2 is a dumping ground for future ideas that may never be built.

1.  Passive Attenuator (The "Hello World" build)
2.  Power Supply (12v AC wall wart based)
3.  Clock source, divider and multiplier
4.  Quantizer
5.  Sequential switch
6.  CV Mixer
7.  Offset/Attenuverter

Casing will be entirely 3d printed.

## Tooling

*   **Schematics & PCB**: KiCad (Recommended) - It is the open-source standard for Eurorack DIY.
*   **Code**: MicroPython (via Thonny IDE).
*   **3D Design**: Onshape.
*   **Slicing/Printing**: Orca Slicer, printed on a Creality K1 Max.

## Project Structure

Each module will have its own folder. It will include:
* Requirements and description
* Build guide and BOM
* Code files as needed

## General Considerations

* Where a microcontroller is used, the Raspberry Pi Pico will be used unless there are very strong reasons not to. 
* Prefer more buttons and controls over a display, but displays may be used where useful.
* Prototype on a breadboard first to learn and understand. Final step will be to build a stripboard and full enclosures.
* The EuroPi source code is included in the reference folder. Use it for important elements like voltage management and power safety.


## Appendix: Phase 2

(TBD)