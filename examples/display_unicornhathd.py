#!/usr/bin/env python3
"""Use the UnicornHATHD display driver to update a Unicorn HAT HD display."""
from matrix_display import Conveyor
from matrix_display.displays import UnicornHATHD
import row_functions as f

conveyor = Conveyor(UnicornHATHD(16, 16).rotation(180))
conveyor.add_row(f.get_sine_wave_canvas, 1, 16, 6)  # >= 1 second refresh
conveyor.add_row(f.get_clock_text_tuple_list, 5)  # >= 5 second refresh
conveyor.add_row(f.get_seconds_text_tuple, 0.25)  # >= 0.25 second refresh
conveyor.play()
