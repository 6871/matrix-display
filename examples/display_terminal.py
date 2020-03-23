#!/usr/bin/env python3
"""Use the Terminal display driver to simulate a LED display in a terminal."""
from matrix_display import Conveyor
from matrix_display.displays import Terminal
import row_functions as f

conveyor = Conveyor(Terminal(16, 16))
conveyor.add_row(f.get_sine_wave_canvas, 1, 16, 6)  # >= 1 second refresh
conveyor.add_row(f.get_clock_text_tuple_list, 5)  # >= 5 second refresh
conveyor.add_row(f.get_seconds_text_tuple, 0.25)  # >= 0.25 second refresh
Terminal.clear_screen()
conveyor.play()
