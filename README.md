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


## Project Goals ##


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

## Phase 1 ##

The following modules are planned for Phase 1 which is the main effort. Phase 2 is a dumping ground for future ideas that may never be built.

1. Clock source, divider and multiplier
2. Quantizer
3. Sequential switch
4. CV Mixer
5. Offset/Attenuverter

## Project Structure ##

Each module will have its own folder. It will include:
* Requirements and description
* Build guide and BOM
* Code files as needed


## Appendix: Phase 2 ##

(TBD)