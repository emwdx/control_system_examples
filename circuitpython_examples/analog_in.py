"""CircuitPython Essentials Analog In example"""
import time
import board
from analogio import AnalogIn

# Connect an analog sensor to the A1 port of the board you are using. This means a 3V, GND, and signal pin must all be connected.
analog_in = AnalogIn(board.A1)

# This function turns the analog reading of the sensor (a number from 0 - 65536) to a voltage.
def get_voltage(pin):
    return (pin.value * 3.3) / 65536

while True:
    print((get_voltage(analog_in),))
    time.sleep(0.1)
