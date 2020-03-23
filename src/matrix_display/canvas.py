#!/usr/bin/env python3
"""Module defining Canvas class."""
import matrix_display.font_5 as font_5
import matrix_display.rgb_colours as rgb_colours


class Canvas:
    """Represents a canvas as a matrix (list of rows) with methods to append
    content.
    """
    def __init__(
            self,
            lpad_count=0,
            row_count=None,
            pad_colour=rgb_colours.black,
            charset=None
    ):
        """By default, initialise canvas with number of rows needed to display
        charset. A number of blank columns can be specified if required
        (useful for scrolling). A number of rows can be defined if auto sizing
        to the charset is not required.

        Parameters
        ----------
        charset : dict
            Optional dictionary of character shapes used to print text to the
            canvas; defaults to font_5x5.lookup
        lpad_count : int
            Optional number of empty columns to left-pad the canvas with;
            useful if know in advance the text will be scrolled in from the
            right
        row_count : int
            Optional number of rows; defaults to the charset height
        pad_colour : (int, int, int)
            Optional pad colour; defaults to rgb_colours.black, i.e. (0, 0, 0)

        Returns
        -------
        None

        Examples
        --------
        >>> from matrix_display import Canvas
        >>> Canvas()
        []
        []
        []
        []
        []
        >>> Canvas(1)
        [ ]
        [ ]
        [ ]
        [ ]
        [ ]
        >>> Canvas(1).rows
        [[(0, 0, 0)], [(0, 0, 0)], [(0, 0, 0)], [(0, 0, 0)], [(0, 0, 0)]]
        >>> Canvas(4,2)
        [    ]
        [    ]
        >>>
        """
        self.charset = font_5.lookup if charset is None else charset
        row_count = len(self.charset['0']) if row_count is None else row_count
        self.rows = [
            [
                pad_colour for __ in range(lpad_count)
            ] for __ in range(row_count)
        ]

        self.append_space = 0  # first character will have no preceding space

    def height(self):
        """Return the current pixel height of the canvas.

        Returns
        -------
        height : int

        Examples
        --------
        >>> from matrix_display import Canvas
        >>> Canvas().append_text('Hello, World!').height()
        5
        >>>
        """
        return 0 if self.rows is None else len(self.rows)

    def width(self):
        """Return the current pixel width of the canvas.

        Returns
        -------
        width : int

        Examples
        --------
        >>> from matrix_display import Canvas
        >>> Canvas().append_text('Hello, World!').width()
        45
        >>>
        """
        if self.rows is None or len(self.rows) == 0:
            return 0
        else:
            return len(self.rows[0])

    def append_canvas(self, canvas, lpad_count=None,
                      pad_colour=rgb_colours.black):
        """Append canvas to this canvas.

        Parameters
        ----------
        canvas : Canvas
            The canvas to append
        lpad_count : int
            Optional custom padding amount between the canvases; default value
            of None lets target canvas decide
        pad_colour : (int, int, int)
            Optional pad colour; defaults to rgb_colours.black, i.e. (0, 0, 0)

        Returns
        -------
        self : Canvas

        Examples
        --------
        >>> from matrix_display import Canvas
        >>> c1 = Canvas().append_text('c1')
        >>> c2 = Canvas().append_text('c2', (0, 255, 255))
        >>> Canvas().append_canvas(c1).append_canvas(c2)
        [    █     ███]
        [    █       █]
        [███ █ ███ ███]
        [█   █ █   █  ]
        [███ █ ███ ███]
        >>>
        """
        if len(canvas.rows) > len(self.rows):
            raise ValueError((
                f"Can't append canvas with row count \"{len(canvas.rows)}\" "
                f"to canvas with row count \"{len(self.rows)}\""
            ))

        lpad_count = self.append_space if lpad_count is None else lpad_count
        row_ctr = 0
        for row in canvas.rows:
            if lpad_count > 0:
                self.rows[row_ctr].extend(
                    [pad_colour for __ in range(lpad_count)])
            self.rows[row_ctr].extend(row)
            row_ctr += 1

        self.append_space = 1  # Precede all subsequent content with a space
        return self

    def append_text(self, text, rgb=(255, 255, 255), unknown_char='█'):
        """Append text to a canvas matrix using the specified RGB colour.

        Parameters
        ----------
        text : str
            The text to append to the canvas
        rgb : (int, int, int)
            Optional RGB colour tuple, defaults to white, i.e. (255, 255, 255)
        unknown_char : str
            If a character in the text parameter does not exist in the
            charset, this character is printed on the canvas instead; the
            default value is '█'

        Returns
        -------
        self : Canvas

        Examples
        --------
        >>> from matrix_display import Canvas
        >>> Canvas().append_text('Hi').append_text('!')
        [█ █ █ █]
        [█ █   █]
        [███ █ █]
        [█ █ █  ]
        [█ █ █ █]
        >>> # If '¶' is not in charset, default unknown_char='█' is used:
        >>> Canvas().append_text('abc¶d')
        [██  █       █████   █]
        [  █ █       █████   █]
        [ ██ ███ ███ █████ ███]
        [█ █ █ █ █   █████ █ █]
        [ ██ ███ ███ █████ ███]
        >>>
        """
        for c in text:
            # Handle characters not in font charset (to a point)
            try:
                c_map = self.charset[c]
            except KeyError:
                try:
                    c_map = self.charset[unknown_char]
                except KeyError:
                    c_map = self.charset['█']

            c_width = len(c_map[0])  # char rows are same length, use 1st row
            row_ctr = 0

            # Append character; and leading space unless at canvas start
            for row in self.rows:
                for col_ctr in range(self.append_space + c_width):
                    if self.append_space == 1 and col_ctr == 0:
                        row.append(rgb_colours.black)
                    else:
                        if c_map[row_ctr][col_ctr - self.append_space] == 0:
                            row.append(rgb_colours.black)
                        else:
                            row.append(rgb)
                row_ctr += 1

            # Precede all subsequent content with a space
            self.append_space = 1
        return self

    def append_text_from_function(self, function):
        """Append text blocks returned by the passed function to the canvas.

        Parameters
        ----------
        function : Callable
            Function returning a list of tuples that each define a string and
            colour; for example, to specify a red 'R', green 'G' and blue 'B'
            the function would return the following:
                [
                    ('R', (255, 0, 0)),
                    ('G', (0, 255, 0)),
                    ('B', (0, 0, 255))
                ]

        Returns
        -------
        self : Canvas

        Examples
        --------
        >>> from matrix_display import Canvas
        >>> def hello_world():
        ...     return [
        ...         ('Hello', (0, 255, 0)),
        ...         (', ', (255, 0, 0)),
        ...         ('World!', (0, 0, 255))
        ...     ]
        ...
        >>> Canvas().append_text_from_function(hello_world)
        [█ █  █  █  █           █   █         █    █ █]
        [█ █ █ █ █  █   █       █   █  █      █    █ █]
        [███ ███ █  █  █ █      █ █ █ █ █ ███ █  ███ █]
        [█ █ █   █  █  █ █  █   █ █ █ █ █ █   █  █ █  ]
        [█ █  ██  █  █  █  █     █ █   █  █    █ ███ █]
        >>>
        """
        for text_block in function():
            text, rgb = text_block
            self.append_text(text, rgb)

        return self

    def to_str(self, show_colour=False, pixel_on='\u2588', pixel_off=' '):
        """Returns a string representation of the canvas that can be displayed
        with Python's print() function. Colourised output is optional and only
        approximates RGB colour; avoid colourised output if writing to log
        files, it introduces significant control-code clutter.

        Parameters
        ----------
        show_colour : Boolean
            Optional parameter to specify whether to include terminal colour
            codes in the output string; defaults to False
        pixel_on : str
            Optional alternate character to represent a non-black pixel; the
            default is a solid block character (unicode '\u2588')
        pixel_off : str
            Optional alternate character to represent a black pixel, the
            default is a space ' '

        Returns
        -------
        text : str
            String representation of the canvas.

        Examples
        --------
        >>> from matrix_display import Canvas
        >>> Canvas().append_text('Hi').to_str()
        '[█ █  ]\n[█ █ █]\n[███  ]\n[█ █ █]\n[█ █ █]'
        >>> print(Canvas().append_text('Hi').to_str())
        [█ █  ]
        [█ █ █]
        [███  ]
        [█ █ █]
        [█ █ █]
        >>> print(Canvas().append_text('BLUE', (0, 0, 255)).to_str(show_colour=True))
        [██  █   █ █ ███]
        [█ █ █   █ █ █  ]
        [██  █   █ █ ██ ]
        [█ █ █   █ █ █  ]
        [██  ███ ███ ███]
        >>>
        """
        text = ''
        row_count = len(self.rows)
        for row_ctr, row in enumerate(self.rows):
            text += '['
            for col in row:
                if col[0] == 0 and col[1] == 0 and col[2] == 0:
                    text += pixel_off
                else:
                    if show_colour:
                        text += self.__term_colour(col) + pixel_on + '\033[0m'
                    else:
                        text += pixel_on
            text += ']' + ('\n' if row_ctr < row_count - 1 else '')
        return text

    def add_rows(self, count=1, pad_colour=rgb_colours.black):
        """Adds rows to the canvas.

        Parameters
        ----------
        count : int
            Optional number of rows to add; defaults to 1
        pad_colour : (int, int, int)
            Optional colour to use for new row; defaults to black

        Returns
        -------
        self : Canvas
        """
        for __ in range(count):
            self.rows.append([pad_colour for __ in range(self.width())])

        return self

    def delete_rows(self, count=1):
        """Delete rows from the canvas.

        Parameters
        ----------
        count : int
            Optional number of rows to delete; defaults to 1

        Returns
        -------
        self : Canvas
        """
        if count > len(self.rows):
            raise ValueError((
                f"Delete failed; delete count \"{count}\" exceeds canvas "
                f"row count \"{len(self.rows)}\""))

        for i in range(len(self.rows) - 1, len(self.rows) - 1 - count, -1):
            del[self.rows[i]]

        return self

    @staticmethod
    def __term_colour(rgb):
        """Evaluate a RGB tuple and attempt to return a similar terminal
        colour code.

        Parameters
        ----------
        rgb : (int, int, int)
            Tuple of 3 int values representing red, green and blue content

        Returns
        -------
        code : str
            String containing the best guess at the terminal colour code for
            the specified rgb parameter
        """
        c = '\033['
        if rgb[0] == 0 and rgb[1] == 0 and rgb[2] == 0:  # black
            c += '90m'
        elif rgb[0] > 0 and rgb[1] == 0 and rgb[2] == 0:  # red
            c += '91m'
        elif rgb[0] == 0 and rgb[1] > 0 and rgb[2] == 0:  # green
            c += '92m'
        elif rgb[0] == 0 and rgb[1] == 0 and rgb[2] > 0:  # blue
            c += '94m'
        elif rgb[0] == 0 and rgb[1] > 0 and rgb[2] > 0:  # assume cyan
            c += '96m'
        elif rgb[0] > 0 and rgb[1] == 0 and rgb[2] > 0:  # assume magenta
            c += '95m'
        elif rgb[0] > 0 and rgb[1] > 0 and rgb[2] == 0:  # assume yellow
            c += '93m'
        else:  # assume white
            c += '97m'  # white
        return c

    def __repr__(self):
        """Return the to_str() representation of this class instead of the
        default Python object description.

        Returns
        -------
        text : str
            String representation of the canvas.
        """
        return self.to_str(show_colour=True)
