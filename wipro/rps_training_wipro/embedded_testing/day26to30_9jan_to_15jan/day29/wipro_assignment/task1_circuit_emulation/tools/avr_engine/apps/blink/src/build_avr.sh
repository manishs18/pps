#!/bin/bash
avr-g++ -g -Os -mmcu=atmega328p -DF_CPU=16000000UL -o blink.elf blink.cpp
avr-objcopy -Obihex -R .eeprom blink.elf blink.hex
echo "Build complete!"