#!/usr/bin/env python3
"""Functions to demonstrate generating matrix_display row data."""
from matrix_display import Canvas
from matrix_display import rgb_colours as rgb
import datetime as dt
import math
from random import randint

colour_ptr = 2  # remember colour for get_sine_wave_canvas function


def get_sine_wave_canvas(*args, **kwargs):
    """Draws 2 waves on a canvas using a different colour to the last call.

    Parameters
    ----------
    args[0] : int
        Number of columns in generated canvas
    args[1] : int
        Number of rows in generated canvas

    Returns
    -------
    canvas : matrix_display.Canvas
        Canvas object with coloured sine wave
    """
    width = args[0]  # pixel width for 1 sine wave
    height = args[1]  # pixel height of sine wave
    canvas = Canvas(row_count=height, lpad_count=width)

    global colour_ptr  # global to persist between calls
    colour_ptr = (colour_ptr + 1) % 3  # colour_ptr's range is 0, 1, 2

    for x in range(width):
        y = int((math.sin((2 * math.pi / width * x)) + 1) / 2 * (height - 1))
        canvas.rows[y][x] = [rgb.red, rgb.green, rgb.blue][colour_ptr]
    return canvas.append_canvas(canvas, 0)  # return 2 waves with 0 space


def get_clock_text_tuple_list(*args, **kwargs):
    """Current date, time and timezone as a list of coloured text tuples.

    Returns
    -------
    datetime : list of tuples
        List of (text, colour) tuples for one display row
    """
    t = dt.datetime.now().astimezone()
    return [
        (t.strftime('%a %m %b'), rgb.cyan),
        (t.strftime(' %H:%M:%S'), rgb.yellow),
        (t.strftime(' %Z %z'), rgb.green)
    ]


def get_seconds_text_tuple(*args, **kwargs):
    """Current time's seconds, in blue.

    Returns
    -------
    seconds : tuple
        A (text, colour) tuple with the time's current seconds in blue
    """
    text = dt.datetime.now().strftime('s:%S')
    return text, rgb.blue


def get_random_canvas_block(*args, **kwargs):
    """Generates a canvas with randomly coloured pixels.

    Parameters
    ----------
    args[0] : int
        Number of columns in generated canvas
    args[1] : int
        Number of rows in generated canvas

    Returns
    -------
    canvas : matrix_display.Canvas
        Canvas object with randomly coloured pixels.
    """
    col_count = 16 if len(args) < 1 else args[0]
    row_count = 16 if len(args) < 2 else args[1]

    canvas = Canvas(row_count=row_count, lpad_count=col_count)
    for r in range(row_count):
        for c in range(col_count):
            canvas.rows[r][c] = (
                randint(0, 255), randint(0, 255), randint(0, 255))
    return canvas
