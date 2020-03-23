#!/usr/bin/env python3
"""Module defining UnicornHATHD display driver class."""
from matrix_display.displays import Display
import sys

try:
    import unicornhathd
except ImportError:
    sys.stderr.write((
        'WARNING: to use a Unicorn HAT HD display install the unicornhathd '
        'package from https://github.com/pimoroni/unicorn-hat-hd\n'
    ))


class UnicornHATHD(Display):
    def __init__(self, row_count, col_count):
        super().__init__(row_count, col_count)

    def set_pixel(self, x, y, r, g, b):
        unicornhathd.set_pixel(x, y, r, g, b)
        return self

    # noinspection PyMethodMayBeStatic
    def draw(self):
        unicornhathd.show()

    def brightness(self, b):
        unicornhathd.brightness(b)
        return self

    def rotation(self, r):
        unicornhathd.rotation(r)
        return self
