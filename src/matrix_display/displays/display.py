#!/usr/bin/env python3
"""Module defining base MatrixDisplay class."""


class Display:
    """Base class for display-specific classes to extend."""
    row_count = 0
    col_count = 0

    def __init__(self, row_count, col_count):
        """Initialise a display object.

        Parameters
        ----------
        row_count : int
            The number of rows in the corresponding physical display
        col_count : int
            The number of columns in the corresponding physical display
        """
        self.row_count = row_count
        self.col_count = col_count

    def set_pixel(self, x, y, r, g, b):
        """Set a display pixel's RGB value (use draw method to display).

        Parameters
        ----------
        x : int
            The x coordinate of the pixel to be updated
        y : int
            The y coordinate of the pixel to be updated
        r : int
            The red component of the pixel to be updated; 0-255
        g : int
            The green component of the pixel to be updated; 0-255
        b : int
            The blue component of the pixel to be updated; 0-255
        """
        pass

    def draw(self):
        """Show current pixel colours (set with set_pixel) on the display."""
        pass
