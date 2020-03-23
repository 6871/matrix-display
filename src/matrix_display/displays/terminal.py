#!/usr/bin/env python3
"""Module defining Terminal display driver class."""
from matrix_display import Canvas
from matrix_display.displays import Display


class Terminal(Display):
    """A mock display that can be displayed as text in a terminal.

    Examples
    --------
    >>> from matrix_display.displays import Terminal
    >>> t = Terminal(16, 16)
    >>> t.set_pixel(13, 13, 255, 0, 0)
    >>> t.set_pixel(14, 14, 0, 255, 0)
    >>> t.set_pixel(15, 15, 0, 0, 255)
    >>> t.draw(move_cursor=False)
    [                                ]
    [                                ]
    [                                ]
    [                                ]
    [                                ]
    [                                ]
    [                                ]
    [                                ]
    [                                ]
    [                                ]
    [                                ]
    [                                ]
    [                                ]
    [                          ██    ]
    [                            ██  ]
    [                              ██]
    >>>
    """
    canvas = None

    def __init__(self, row_count, col_count):
        """Initialise Terminal object with requested size."""
        super().__init__(row_count, col_count)
        self.canvas = Canvas(row_count=row_count, lpad_count=col_count)

    def set_pixel(self, x, y, r, g, b):
        """Sets a pixel's RGB value.

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
        self.canvas.rows[x][y] = (r, g, b)

    def draw(self, move_cursor=True, wide=True):
        """Prints a textual representation of the display.

        Parameters
        ----------
        move_cursor : bool
            Determines if the cursor is moved to the top left of the screen
            before the textual representation of the display is printed
        wide : bool
            If True (default) use 2 terminal characters per pixel to try and
            get row and column size more equal; set to False to optimise space
        """
        if move_cursor:
            print('\033[1;1H')  # move cursor to top left of terminal

        if wide:
            print(self.canvas.to_str(
                show_colour=True, pixel_on='\u2588\u2588', pixel_off='  '))
        else:
            print(self.canvas.to_str(show_colour=True))

        if move_cursor:
            print('\nCTRL-C to exit')

    @staticmethod
    def clear_screen():
        """Reset the terminal display."""
        print('\033c')

    @staticmethod
    def cursor_hide():
        """Hide the terminal cursor."""
        print('\033[?25l')
        
    @staticmethod
    def cursor_show():
        """Show the terminal cursor."""
        print('\033[?25h')
